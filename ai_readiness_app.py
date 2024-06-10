from flask import (
    Flask,
    render_template,
    request
) 

import os

from functions.userinterfacefunctions import scoring as sc, datavisualisation, process_responses, resultsdoc

app = Flask("ai-readiness") 

# index - quiz
@app.route("/")
def index():
    print('index')
    return render_template('index.html')

# results
@app.route("/results", methods=['POST'])
def results():
    print('results')
    scores = process_responses.ProcessResponses.process_responses()
    average_score, overall_message = sc.Scoring.average_score(scores)
    average_score_solution, overall_message_solution = sc.Scoring.average_score_solution(scores)
    average_score_organization, overall_message_organization = sc.Scoring.average_score_organization(scores)
    graph = datavisualisation.DataVisualisaton.plot_chart(scores)
    get_in_touch = sc.Scoring.get_in_touch()
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
