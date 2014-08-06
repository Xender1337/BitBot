#!/usr/bin/env python

# -------------------------------------------------------------------------------------------------------------------- #
__author__ = 'Xender'
# -------------------------------------------------------------------------------------------------------------------- #


### IMPORT
import BitstampAPI
import os
import sys
from datetime import datetime
from bitstampy import api
# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")
sys.path.append('../')
from Trade.models import BtcValue, EurUsd, BitstampUser


print "\n###############################\n####     Start of Cron     ####\n###############################\n"
APIPublic = BitstampAPI.API()
APIPrivate = api

print "Date is : " + str(datetime.now())

### ---- Recuperation des infos necessaire pour BtcRate
print "\n######  Get Info of Btc  ######"
rate = APIPublic.GetRate()
print "The current info for bitcoin is : " + str(rate)
### ---- Mise en BDD de BtcRate
BtcValue(rate=rate['last'],
         high=rate['high'],
         low=rate['low'],
         ask=rate['ask'],
         volume=rate['volume']).save()

### ---- Recuperation des infos necessaire pour Eur/Usd
print "\n####  Get Info of Usd/Eur  ####"
EurUsdValue = APIPublic.GetEurUsd()
print "The current rate for EUR/USD is : " + str(EurUsdValue)
### ---- Mise en BDD de EurUsd
EurUsd(buy=EurUsdValue['buy'],
       sell=EurUsdValue['sell']).save()


### ---- Recuperation des infos pour chaque Bitstamp User
print "\n# Get Info for Bitstamp User  #"
for a_user in BitstampUser.objects.all():
    Secret = a_user.SecretKey
    Public = a_user.PublicKey
    UserID = a_user.UserID

    print "Get Info for ' + a_user.AccountName + ' Account"
    AccountInfo = APIPrivate.account_balance(str(UserID), str(Public), str(Secret))
    a_user.UsdBalance = AccountInfo['usd_balance']
    a_user.UsdAvailable = AccountInfo['usd_available']
    a_user.UsdReserved = AccountInfo['usd_reserved']
    a_user.BtcBalance = AccountInfo['btc_balance']
    a_user.BtcAvailable = AccountInfo['btc_available']
    a_user.BtcReserved = AccountInfo['btc_reserved']
    a_user.Fee = AccountInfo['fee']
    a_user.save()
    print "Info for this account id : " + str(AccountInfo)




print "\n###############################\n#####     End of Cron     #####\n###############################\n"
