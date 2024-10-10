import datetime as dt
import time as t
from flask import request
from google.cloud import bigquery
client = bigquery.Client()
from functions.userinterfacefunctions.scoring import Scoring as sc
import uuid

class DatabasePush:

    def get_email(data):

        email_address = str(data["email"])
        return email_address

    def get_results_for_db(data):
        q1 = float(data["q1"])
        q2 = float(data["q2"])
        q3 = float(data["q3"])
        q4 = float(data["q4"])
        q5 = float(data["q5"])
        q6 = float(data["q6"])
        q7 = float(data["q7"])
        q8 = float(data["q8"])
        q9 = float(data["q9"])
        q10 = float(data["q10"])

        scores = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]


        return scores

    def get_averages(data):
        scores = DatabasePush.get_results_for_db(data)
        avg_all = sc.average_score(scores)
        avg_org = sc.average_score_organization(scores)
        avg_sol = sc.average_score_solution(scores)

        return avg_all, avg_org, avg_sol


    def create_db_row(data):
        
        id = int(t.time() * 1000)
        timestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email = DatabasePush.get_email(data) 
        scores = DatabasePush.get_results_for_db(data)
        name = data['name']
        comments = data['comments']
        mailing_list = True if data['mailing_list'] == "on" else False
        follow_up = True if data['follow_up'] == "on" else False
        experts_recommended = str(sc.experts(scores)[1][0] + ", " + sc.experts(scores)[2][0])
        weakest_area = sc.worst_question(scores)[1]
        strongest_area = sc.best_question(scores)[1]
        db_list = [id, timestamp, name, email, *scores, sc.average_score_organization(scores)[0], sc.average_score_solution(scores)[0], sc.average_score(scores)[0], comments, mailing_list, follow_up, experts_recommended, weakest_area, strongest_area]

         # columns:
        # (response_id, timestamp, responder_name, responder_email, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, org_score,
        # solution_score, overall_score, comments, mailing_list, follow_up, experts_recommended, weakest_area, strongest_area) {db_list}"
        
        return db_list

    def push_responses(data):
        
        db_list = str(DatabasePush.create_db_row(data)).replace('[', '').replace(']', '')
        push_query_SQL = f"INSERT INTO `ai-readiness-matrix.matrixdata.results` (response_id, timestamp, responder_name, responder_email, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, org_score,         solution_score, overall_score, comments, mailing_list, follow_up, experts_recommended, weakest_area, strongest_area) VALUES ({db_list})"
        push_query_job = client.query(push_query_SQL)
        status = push_query_job.state
        return status
