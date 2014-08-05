#!/usr/bin/env python
__author__ = 'Naze'

import os

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

from Trade.models import BtcValue, Average, AlgOption


# -------------------------------------------------------------------------------------------------------------------- #

current_rate = BtcValue.objects.all()[:1]
current_rate = current_rate.rate

lastAverage = Average.objects.all()[:1]
monthAverage = lastAverage.monthAverage
dayAverage = lastAverage.dayAveraga


options = {0 : Buying,
           1 : Selling,}

options[AlgOption.Status]()

def Buying():
    if current_rate < monthAverage && current_rate < dayAverage:
        AlgOption.BuyRate = current_rate
        buy()
        AlgOption.Status = 1

def Selling():
    if current_rate >= AlgOption.BuyRate + 10:
        sell()
    AlgOption.Status = 0

def buy():


def sell():