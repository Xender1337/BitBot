#!/usr/bin/env python
__author__ = 'Xender'

import memcache
import os
from pprint import pprint
import json
from bitstampy import api

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

from django.core.cache import cache, get_cache
from Trade.models import BtcValue, BitstampUser

'''
print "Start of Test"

cache.set('test', BtcValue.objects.all())
cache1 = cache.get('test')

print cache1

client = memcache.Client(["127.0.0.1:11211"])
print "Success define client"
client.set("toto", BtcValue.objects.all(), )

print "Success for Set"

result = client.get("toto")
print "Result of request = " + str(result)
'''

print "Start Toto Test"

API = api

for a_user in BitstampUser.objects.all():
    Secret = a_user.SecretKey
    Public = a_user.PublicKey
    UserID = a_user.UserID

    result = API.user_transactions(str(UserID), str(Public), str(Secret))
    print pprint(result)
    pprint(result, stream=None, indent=4)
    pprint()

print "End Toto Test"