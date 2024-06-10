from flask import request


class ProcessResponses():

    def process_responses():

        q1 = int(request.form['q1'])
        q2 = int(request.form['q2'])
        q3 = int(request.form['q3'])
        q4 = int(request.form['q4'])
        q5 = int(request.form['q5'])
        q6 = int(request.form['q6'])
        q7 = int(request.form['q7'])
        q8 = int(request.form['q8'])
        q9 = int(request.form['q9'])
        q10 = int(request.form['q10'])

        scores = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
       
        return scores
