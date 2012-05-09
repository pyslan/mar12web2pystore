# coding: utf-8
import urllib
import json

def get_tweets():
    produto = request.vars.produto
    url = "http://search.twitter.com/search.json?%s"
    params = dict(q=produto, result_type='mixed', count=5)
    result = urllib.urlopen(url % urllib.urlencode(params)).read()
    tweets = json.loads(result)
    return dict(tweets=tweets)
