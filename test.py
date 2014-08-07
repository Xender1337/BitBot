#!/usr/bin/env python
__author__ = 'Xender'

import memcache
import os

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

from django.core.cache import cache, get_cache
from Trade.models import BtcValue

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