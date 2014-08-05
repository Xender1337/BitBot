#!/usr/bin/env python
__author__ = 'Naze'

import os

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

from Trade.models import BtcValue, Average


# -------------------------------------------------------------------------------------------------------------------- #

current_rate = BtcValue.objects.filter[:1]
buy_rate = 0

optionNbr = 0
options = {0 : Buying,
           1 : Selling,}

def Buying():
    if current_rate < Average.object.filter(Average.monthAverage)[:1] & current_rate < Average.objects.filter(Average.dayAverage)[:1]:
        buy_rate = current_rate
         buy()
        optionNbr = 1

def Selling():
    if current_rate >= buy_rate:
        sell()
    optionNbr = 0

def buy():


def sell():