#!/usr/bin/env python

# -------------------------------------------------------------------------------------------------------------------- #

__author__ = 'Xender'
# -------------------------------------------------------------------------------------------------------------------- #


### IMPORT
import BitstampAPI
import os
import sys
import datetime
# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")
sys.path.append('../')
from Trade.models import BtcRate


print "\n###############################\n####     Start of Cron     ####\n###############################\n"
API = BitstampAPI.API()
rate = API.GetRate()

### ---- Mise en BDD de BtcRate
BtcRate(rate=rate['last'],
        high=rate['high'],
        low=rate['low'],
        ask=rate['ask'],
        volume=rate['volume']).save()

### ---- Debug
print datetime.datetime.now()
print "The current info for bitcoin is : " + str(rate)

print "\n###############################\n#####     End of Cron     #####\n###############################\n"
