import datetime
from flask import request
from google.cloud import bigquery
client = bigquery.Client()
from functions.userinterfacefunctions.scoring import Scoring as sc


class DatabasePush:

    def get_email():

        email_address = float(request.form["email"])
        return email_address

    def get_results_for_db():
        q1 = float(request.form["q1"])
        q2 = float(request.form["q2"])
        q3 = float(request.form["q3"])
        q4 = float(request.form["q4"])
        q5 = float(request.form["q5"])
        q6 = float(request.form["q6"])
        q7 = float(request.form["q7"])
        q8 = float(request.form["q8"])
        q9 = float(request.form["q9"])
        q10 = float(request.form["q10"])

        scores = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

        # todo: json / columns

        return scores

    def get_averages(scores):
        avg_all = sc.average_score(scores)
        avg_org = sc.average_score_organization(scores)
        avg_sol = sc.average_score_solution(scores)

        return avg_all, avg_org, avg_sol

        # todo: json / columns

    def create_db_row(data, email, scores):

        #generate id
        id = ""
        timestamp = datetime.now()
        name = data.name
        comments = data.comments
        mailing_list = data.mailing_list
        follow_up = data.follow_up
        experts_recommended = data.experts_recommended
        worst_score = sc.worst_question(scores)
        weakest_area = worst_score[1] #todo: verify
        strongest_area = data.strongest_area
       
        db_list = []
        db_list.append(id, timestamp, name, email)

        for s in scores:
            db_list.append(s)

        

        db_list.append(sc.average_score_organization, sc.average_score_solution, sc.average_score, comments, mailing_list, follow_up, experts_recommended, weakest_area, strongest_area)


         # columns:
        # (response_id, timestamp, responder_name, responder_email, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, org_score,
        # solution_score, overall_score, comments, mailing_list, follow_up, experts_recommended, weakest_area, strongest_area) {db_list}"
        
        return db_list

    def push_responses(db_list):
        
        push_query_SQL = f"INSERT INTO `ai-readiness-matrix.matrixdata.results` 
        (response_id, timestamp, responder_name, responder_email, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, org_score,
        solution_score, overall_score, comments, mailing_list, follow_up, experts_recommended, weakest_area, strongest_area) {db_list}"
        push_query_job = client.query(push_query_SQL)
        print(push_query_job)

        return "ok"
