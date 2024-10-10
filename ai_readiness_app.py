from flask import (
    Flask,
    render_template,
    request
) 
import json
import os

from functions.datafunctions.database_pull import DatabasePull as db
from functions.datafunctions.database_push import DatabasePush as dp


from functions.userinterfacefunctions import scoring as sc, datavisualisation as dv, process_responses as proc, resultsdoc as rd

app = Flask("ai-readiness") 


# index - quiz
@app.route("/")
def index():

    questions_list = db.pull_questions()
    
    return render_template('index.html', questions_list=questions_list)

# results
@app.route("/results", methods=['POST'])
def results():
    print('results')
    data = request.form
    dp.push_responses(data)
    
    scores = proc.ProcessResponses.process_responses()
    print(scores)

    average_score, overall_message = sc.Scoring.average_score(scores)
    average_score_solution, overall_message_solution = sc.Scoring.average_score_solution(scores)
    average_score_organization, overall_message_organization = sc.Scoring.average_score_organization(scores)
    
    graph = dv.DataVisualisaton.plot_chart(scores)
    experts = sc.Scoring.experts(scores)
         # topic = experts[0]
        # leader = experts[1]
        # supporter = experts[2]

    #todo: object here
        
    doc = "" #rd.ResultsDoc()
    results_data = {
        "average_score" : average_score,
        "overall_message" : overall_message,
        "average_score_organization" : average_score_organization,
        "overall_message_organization" : overall_message_organization,
        "average_score_solution" : average_score_solution,
        "overall_message" : overall_message,
        "experts" : experts

    }
    return render_template('results.html', graph=graph, 
                           results_data=results_data)

# about
@app.route("/about")
def about():
    print('about')
    return render_template('about.html')

@app.route("/report")
def report():
    rd.download_report()
    print('report')
    return render_template('thankyou.html')

# debugging
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
