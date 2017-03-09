from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_triangle import Triangle
from flask_jsglue import JSGlue
import facebook_scrape_events as f

app = Flask(__name__)
Bootstrap(app)
Triangle(app)
jsglue = JSGlue(app)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

# @app.route('/gigs')
# def scrape():
#     return f.scrapeFacebookEvents(request.query_string.decode("utf-8"))
#
# @app.route('/gigsearch')
# def gigsearch():
#     return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)