import urllib
import simplejson
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import functions
import os

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('index.html', tweet="")

@app.route('/compose', methods=['POST', 'GET'])
def compose():
    query = request.form["query"]
    tweet = functions.searchTweets(query)
    #Scale will default to minor because minor scales are cooler
    scale = 1
    if ":)" in query:
        scale = 0
    return render_template('index.html', tweet=tweet)

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port, debug="true")
