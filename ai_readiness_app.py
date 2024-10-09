from flask import (
    Flask,
    render_template,
    request
) 
import json
import os

from functions.datafunctions.database_pull import *


from functions.userinterfacefunctions import scoring as sc, datavisualisation as dv, process_responses as proc, resultsdoc as rd

app = Flask("ai-readiness") 


# index - quiz
@app.route("/")
def index():

    questions_list = DatabasePull.pull_questions()
    
    return render_template('index.html', questions_list=questions_list)

# results
@app.route("/results", methods=['POST'])
def results():
    print('results')
    
    scores = proc.ProcessResponses.process_responses()
    print(scores)

    average_score, overall_message = sc.Scoring.average_score(scores)
    average_score_solution, overall_message_solution = sc.Scoring.average_score_solution(scores)
    average_score_organization, overall_message_organization = sc.Scoring.average_score_organization(scores)
    
    graph = dv.DataVisualisaton.plot_chart(scores)
    get_in_touch = sc.Scoring.get_in_touch(scores)
    doc = rd.ResultsDoc()
    return render_template('results.html', graph=graph, 
                           average_score=average_score, 
                           overall_message = overall_message,
                           average_score_organization=average_score_organization,
                           overall_message_organization=overall_message_organization, 
                           average_score_solution=average_score_solution,
                           overall_message_solution=overall_message_solution,
                           get_in_touch = get_in_touch)

# about
@app.route("/about")
def about():
    print('about')
    return render_template('about.html')

@app.route("/report")
def report():
    resultsdoc.download_report()
    print('report')
    return render_template('thankyou.html')

# debugging
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
