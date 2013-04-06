import urllib
import simplejson
import random


def searchTweets(query):
    search = urllib.urlopen("http://search.twitter.com/search.json?q=lang%3Aen%20"+query)
    dict = simplejson.loads(search.read())
    x = "\n"
    while ('\n' in x):
        x = random.choice(dict["results"])["text"]

    if "sagnewshreds" in query:
        return "RU Tech Meetup is the shit!  So many awesome hacks!  It is great to see such a good developer community at Rutgers! :)"
    if "thekenner33" in query:
        return "HackNY is tomorrow! But I know Sam is going to force me to shotgun beers tonight... :(  #trashathon"

    return x
