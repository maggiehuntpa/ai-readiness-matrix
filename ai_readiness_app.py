from flask import (
    Flask,
    render_template,
    request
) 

import os

from functions.userfunctions import scoring, datavisualisation, process_responses

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
    average_score = scoring.Scoring.average_score(scores)
    average_score_solution = scoring.Scoring.average_score_solution(scores)
    average_score_organization = scoring.Scoring.average_score_organization(scores)
    graph = datavisualisation.DataVisualisaton.plot_chart(scores)
    return render_template('results.html', graph=graph, average_score=average_score, average_score_organization=average_score_organization, average_score_solution=average_score_solution)

# about
@app.route("/about")
def about():
    print('about')
    return render_template('about.html')

# debugging
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
