from flask import request


class ProcessResponses():

    def process_responses():

        q1 = float(request.form['q1'])
        q2 = float(request.form['q2'])
        q3 = float(request.form['q3'])
        q4 = float(request.form['q4'])
        q5 = float(request.form['q5'])
        q6 = float(request.form['q6'])
        q7 = float(request.form['q7'])
        q8 = float(request.form['q8'])
        q9 = float(request.form['q9'])
        q10 = float(request.form['q10'])

        scores = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
       
        return scores
