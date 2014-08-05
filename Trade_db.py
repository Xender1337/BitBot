#!/usr/bin/env python

# -------------------------------------------------------------------------------------------------------------------- #

__author__ = 'Xender'
# -------------------------------------------------------------------------------------------------------------------- #


### IMPORT
import os
import time
import re
from decimal import *
import datetime
from time import mktime

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")
from Trade.models import BtcValue

BtcValue.objects.all().delete()
file = open("test", mode='r')

while file.readline():
    current_line = file.readline()
    #print current_line
    res = re.match(r'(\d{4})-(\d{2})-(\d{2}).(\d{2}):(\d{2}):\d+.(\d+).(\d+).(\d+).(\d+).', current_line)

    if res:
        print "Years is : " + res.group(1) + \
              " // Month is : " + res.group(2) + \
              " // Days is : " + res.group(3) + \
              " // Hour : " + res.group(4) + \
              " // Minute : " + res.group(5) + \
              " // Open : " + res.group(6) + '.' + res.group(7) + \
              " // High : " + res.group(8) + '.' + res.group(9)


        result = str(res.group(1)) + '-' + \
                 str(res.group(2)) + '-' + \
                 str(res.group(3)) + ' ' + \
                 str(res.group(4)) + ':' + \
                 str(res.group(5))
        print result
        Open = Decimal(str(res.group(6)) + '.' + str(res.group(7)))
        print Open

        #DateTime = time.strptime(result, "%d-%m-%y %H:%M")
        #print repr(DateTime)

        BtcValue(rate=Open, high=Open, low=Open, ask=Open, volume=0, date=result).save()