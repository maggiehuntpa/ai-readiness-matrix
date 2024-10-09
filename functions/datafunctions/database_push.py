from flask import request

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

    def create_db_object():
        # todo: json / columns

        db_object = {}

        return db_object

    def push_responses():
        # todo pushg to db

        return "ok"
