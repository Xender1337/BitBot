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
AlgOption(Status=0, BuyRate=0, cpt=0, date=current_date).save()

print "debut Trade"
while current_date < end_date:

    print "Changement de la date"
    #Changement de la date
    cnt -= 1
    td = timedelta(days=cnt)
    current_date = end_date - td

    print "Recuperation de la valeur actuelle du cour"
    allBtcValue = BtcValue.objects.order_by('-date').all()[1]
    current_rate = allBtcValue.rate


    print "Recuperation des moyennes du cour"
    lastAverage = Average.objects.all()[0]
    monthAverage = lastAverage.monthAverage
    dayAverage = lastAverage.dayAverage

    def sell():
        a = AlgOption.cpt + 1
        AlgOption(cpt=a).save()

    def buying():
        print "buying"
        if current_rate < monthAverage and current_rate < dayAverage:
            AlgOption.BuyRate = current_rate
            #buy()
        AlgOption.objects.all().delete()
        AlgOption(Status=1).save()

    def selling():
        print "selling"
        if current_rate >= AlgOption.BuyRate + 10:
            sell()
        AlgOption.objects.all().delete()
        AlgOption(Status=0).save()

    options = {0: buying,
               1: selling}


    cursor = AlgOption.objects.all()[0]
    options[cursor.Status]()

print "Fin du trade"
#print "Nombre de trade : " + AlgOption.cpt