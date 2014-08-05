__author__ = 'Xender'

import json
import urllib2

#------------------------------------------ Request for Bitstamp API --------------------------------------------------#


class BtcAPI(object):

    def __init__(self):
        self.result = dict

#-------Request for Bitstamp
    def Get_Info(self):
        url = "https://www.bitstamp.net/api/ticker/"
        print "Request for Bitstamp to get Info"
        try:
            request = urllib2.urlopen(url).read()
            return json.loads(request)
        except:
            print "Request Error"



