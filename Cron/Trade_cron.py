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
from Trade.models import BtcValue, EurUsd


print "\n###############################\n####     Start of Cron     ####\n###############################\n"
API = BitstampAPI.API()

### ---- Recuperation des infos necessaire pour BtcRate
rate = API.GetRate()
### ---- Mise en BDD de BtcRate
BtcValue(rate=rate['last'],
        high=rate['high'],
        low=rate['low'],
        ask=rate['ask'],
        volume=rate['volume']).save()

### ---- Recuperation des infos necessaire pour Eur/Usd
EurUsdValue = API.GetEurUsd()
### ---- Mise en BDD de EurUsd
EurUsd(buy=EurUsdValue['buy'],
       sell=EurUsdValue['sell']).save()

### ---- Debug
print datetime.datetime.now()
print "The current info for bitcoin is : " + str(rate)
print "The current rate for EUR/USD is : " + str(EurUsdValue)

print "\n###############################\n#####     End of Cron     #####\n###############################\n"
