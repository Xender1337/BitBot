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
AlgOption.Status = 0

print "debut Trade"
while current_date < end_date:

    #Changement de la date
    cnt -= 1
    td = timedelta(days=cnt)
    current_date = end_date - td

    #recuperation de la valeur actuelle du cour
    allBtcValue = BtcValue.objects.order_by('-date').all()[1]
    current_rate = allBtcValue.rate

    #recuperation des moyennes du cour
    lastAverage = Average.objects.all()[0]
    monthAverage = lastAverage.monthAverage
    dayAverage = lastAverage.dayAverage



    def sell():
        AlgOption.cpt += 1

    def buying():
        print "buying"
        if current_rate < monthAverage and current_rate < dayAverage:
            AlgOption.BuyRate = current_rate
            #buy()
        AlgOption.objects.all().delete()
        AlgOption.Status = 1

    def selling():
        print "selling"
        if current_rate >= AlgOption.BuyRate + 10:
            sell()
        AlgOption.objects.all().delete()
        AlgOption.Status = 0

    options = {0: buying,
               1: selling}

    print AlgOption.Status
    cursor = AlgOption.objects.all()[0]
    #options[cursor.Status]()

print "Fin du trade"
#print "Nombre de trade : " + AlgOption.cpt