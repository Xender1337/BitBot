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
#AlgOption(Status=0, BuyRate=0, cpt=0, date=current_date).save()
cursor = 0

print "debut Trade"
while current_date < end_date:

    print "Changement de la date"
    #Changement de la date
    cnt -= 1
    td = timedelta(days=cnt)
    current_date = end_date - td
    print current_date

    print "Recuperation de la valeur actuelle du cour"
    #BtcValue = BtcValue.objects.order_by('-date').all()[1]
    BtcValue = BtcValue.objects.filter(date__gt=current_date)[0]
    current_rate = BtcValue.rate
    print current_rate

    if cursor == 0:
        #def buying():
            print "buying"
            print "Recuperation des moyennes du cour"
            #lastAverage = Average.objects.all()[0]
            #monthAverage = lastAverage.monthAverage
            #dayAverage = lastAverage.dayAverage

            cpt = 0
            add = 0

            for value in BtcValue.objects.filter(date__gte=datetime.now()-timedelta(days=30)):
                cpt += 1
                add += value.rate

            monthAverage = add/cpt
            print "Average month :" + str(monthAverage)

            add = 0
            cpt = 0

            for value in BtcValue.objects.filter(date__gte=current_date-timedelta(days=1)):
                cpt += 1
                add += value.rate

            dayAverage = add/cpt
            print 'Average day :' + str(dayAverage)

            if current_rate < monthAverage and current_rate < dayAverage:
                print "current_rate: " + str(current_rate) + " < " + str(monthAverage) + " et " + str(dayAverage)
                #buy()
                algoption = AlgOption.objects.order_by('-date').all()[0]
                AlgOption(Status=1, BuyRate=current_rate, cpt=algoption.cpt, date=current_date).save()
                cursor = 1

    if cursor == 1:
        #def selling():
            print "selling"
            algoption = AlgOption.objects.order_by('-date').all()[0]
            if current_rate >= algoption.BuyRate + 10:
                a = algoption.cpt + 1
                #sell()
                AlgOption(Status=0, cpt=a, date=current_date).save()
                cursor = 0

print "Fin du trade"
print "Nombre de trade : " + AlgOption.cpt