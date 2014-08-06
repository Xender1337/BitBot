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


def MonthAverage(date):
    cpt = 0
    add = 0
    for value in BtcValue.objects.filter(date__gte=date-timedelta(days=30)):
        cpt += 1
        add += value.rate
    monthAverage = add/cpt
    return monthAverage


def DayAverage(date):
    add = 0
    cpt = 0
    for value in BtcValue.objects.filter(date__gte=date-timedelta(days=1)):
        cpt += 1
        add += value.rate
    dayAverage = add/cpt
    return dayAverage

print "\n################################\n####     Debut Du Trade     ####\n################################\n"
while current_date < end_date:

    print "# Changement de la date #"
    td = timedelta(days=cnt)
    current_date = end_date - td
    print str(current_date)+"\n"

    print "# Recuperation des moyennes du cour #"
    #lastAverage = Average.objects.all()[0]
    #monthAverage = lastAverage.monthAverage
    #dayAverage = lastAverage.dayAverage

    monthAverage = MonthAverage(current_date)
    dayAverage = DayAverage(current_date)

    print "Month : " + str(monthAverage)
    print "Day :   " + str(dayAverage) + "\n"

    print "# Recuperation de la valeur actuelle du cour #"
    #BtcValue = BtcValue.objects.order_by('-date').all()[1]
    #BtcValue = BtcValue.objects.filter(date__gt=current_date)[0]
    #current_rate = BtcValue.rate
    #print current_rate

    current_rate = 600

    if cursor == 0:
        #def buying():
            print "\n########################\n####     Buying     ####\n########################\n"

            if current_rate < monthAverage and current_rate < dayAverage:
                print "Achat : " + str(current_rate) + " < " + str(monthAverage) + " et " + str(dayAverage) + "\n"
                #buy()
                algoption = AlgOption.objects.order_by('-date').all()[0]
                AlgOption(Status=1, BuyRate=current_rate, cpt=algoption.cpt, date=current_date).save()
                cursor = 1
            else:
                print "Pas d achat \n"


    if cursor == 1:
        #def selling():
            print "\n######################### n\n####     Selling     ####\n#########################\n"
            algoption = AlgOption.objects.order_by('-date').all()[0]
            if current_rate >= algoption.BuyRate + 10:
                a = algoption.cpt + 1
                #sell()
                AlgOption(Status=0, cpt=a, date=current_date).save()
                cursor = 0
    cnt -= 1

print "Fin du trade"
print "Nombre de trade : " + AlgOption.cpt