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

for value in BtcValue.objects.all().filter(date__gt=current_date):

    current_date = value.date
    print current_date

    #lastAverage = Average.objects.all()[0]
    #monthAverage = lastAverage.monthAverage
    #dayAverage = lastAverage.dayAverage

    monthAverage = MonthAverage(current_date)
    dayAverage = DayAverage(current_date)

    #BtcValue = BtcValue.objects.order_by('-date').all()[1]
    current_rate = value.rate

    if cursor == 0:
        #def buying():

            if current_rate < monthAverage and current_rate < dayAverage:
                #buy()
                print "\n########################\n####     Achete     ####\n########################\n"
                algoption = AlgOption.objects.order_by('-date').all()[0]
                AlgOption(Status=1, BuyRate=current_rate, cpt=algoption.cpt, date=current_date).save()
                cursor = 1

    if cursor == 1:
        #def selling():
            algoption = AlgOption.objects.order_by('-date').all()[0]
            if current_rate >= algoption.BuyRate + 10:
                print "\n########################\n####     Vendu     ####\n########################\n"
                a = algoption.cpt + 1
                #sell()
                AlgOption(Status=0, BuyRate=current_rate, cpt=a, date=current_date).save()
                cursor = 0

print "Fin du trade"

compteur = AlgOption.objects.order_by('-date').all()[0]
print "Nombre de trade : " + compteur.cpt