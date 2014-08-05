__author__ = 'Xender'

import urllib2
import json
import hmac
import hashlib
from time import time


class API(object):
    def __init__(self):
        self.result = dict()
        self.nonce = int(time())

    def GetRate(self):
        url = "https://www.bitstamp.net/api/ticker/"
        request = urllib2.urlopen(url).read()
        result = json.loads(request)
        #print json.dumps(result, indent=4, separators=(',', ': ')) + '\n'
        self.result["Rate"] = {"volume": result['volume'],
                               "last": result['last'],
                               "bid": result['bid'],
                               "high": result['high'],
                               "low": result['low'],
                               "ask": result['ask']}
        #print self.result
        return self.result['Rate']

    def GetEurUsd(self):
        url = "https://www.bitstamp.net/api/eur_usd/"
        request = urllib2.urlopen(url).read()
        result = json.loads(request)
        #print json.dumps(result, indent=4, separators=(',', ': ')) + '\n'
        self.result["EurUsd"] = {"buy": result['buy'],
                                 "sell": result['sell']}
        return self.result['EurUsd']


    #def GetBalance(self, APIKey):

