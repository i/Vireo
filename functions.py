import urllib
import simplejson
import random


def searchTweets(query):
    search = urllib.urlopen("http://search.twitter.com/search.json?q=lang%3Aen%20"+query)
    dict = simplejson.loads(search.read())
    x = "\n"
    if not "results" in dict:
        return "Error @Vireo no tweets loaded #fail #lame"
    
    while ('\n' in x):
        x = random.choice(dict["results"])["text"]

    return x
