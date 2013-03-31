from flask import Flask, render_template, Response
import functions
import composer
import os

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/compose/<search>', methods=['POST', 'GET'])
def compose(search):
    def generate(tweet, mood):
        melodyList = composer.melodize(tweet, mood)
        midi = composer.midFile(melodyList)
        yield midi

    tweet = functions.searchTweets(search)
    if tweet is None:
        return None
    #Scale will default to minor because minor scales are cooler
    mood = 1
    if ":)" in search:
        mood = 0

    resp = Response(generate(tweet, mood), mimetype='audio/midi')
    resp.set_cookie('tweet', tweet)
    return resp

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="true")
