#!/usr/bin/env python
__author__ = 'Naze'

import os
from datetime import timedelta, datetime

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

from Trade.models import BtcValue, Average, AlgOption

# -------------------------------------------------------------------------------------------------------------------- #

end_date = datetime.now()
cnt = 30
td = timedelta(days=cnt)
current_date = end_date - td

while current_date < end_date:

    cnt -= 1
    td = timedelta(days=cnt)
    current_date = end_date - td

    allBtcValue = BtcValue.objects.all()[:1]
    current_rate = allBtcValue.rate

    lastAverage = Average.objects.all()[:1]
    monthAverage = lastAverage.monthAverage
    dayAverage = lastAverage.dayAveraga



    def sell():
        AlgOption.cpt += 1

    def buying():
        if current_rate < monthAverage and current_rate < dayAverage:
            AlgOption.BuyRate = current_rate
            #buy()
            AlgOption.Status = 1

    def selling():
        if current_rate >= AlgOption.BuyRate + 10:
            sell()
        AlgOption.Status = 0


    options = {0: buying,
               1: selling}

    options[AlgOption.Status]()

print "nombre de trade : " + AlgOption.cpt