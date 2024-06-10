from flask import (
    Flask,
    render_template
) 

import os

app = Flask("ai-readiness") 

#index - quiz

@app.route("/")
def app():
    print('app')
    return render_template('index.html')


#results
@app.route("/results")
def reults():
    print('results')
    return render_template('results.html')


#results
@app.route("/about")
def app():
    print('about')
    return render_template('about.html')

#debugging
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))