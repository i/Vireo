import urllib
import simplejson
import random
from constants import *
from TwitterSearch import *

def searchTweets(query):
    try:
        tso = TwitterSearchOrder()
        tso.setKeywords([query])
        tso.setLanguage('en')
        tso.setCount(1)
        tso.setIncludeEntities(False)

        ts = TwitterSearch(
            consumer_key = consumer_key,
            consumer_secret = consumer_secret,
            access_token = access_token,
            access_token_secret = access_token_secret
         )

        for tweet in ts.searchTweetsIterable(tso):
            return tweet['text']

    except TwitterSearchException as e:
        return 'Error @Vireo no tweets loaded #fail #lame'
