import urllib
import simplejson
import random


def searchTweets(query):
    search = urllib.urlopen("http://search.twitter.com/search.json?q=lang%3Aen%20"+query)
    dict = simplejson.loads(search.read())
    x = "\n"
    while ('\n' in x):
        x = random.choice(dict["results"])["text"]

    if query is "sagnewshreds":
        return "RU Tech Meetup is the shit!  So many awesome hacks!  It is great to see such a good developer community at Rutgers! :)"
    if query is "thekenner33":
        return "HackNY is tomorrow! But I know Sam is going to force me to shotgun beers tonight... :(  #trashathon"

    return x
