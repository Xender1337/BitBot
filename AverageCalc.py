#!/usr/bin/env python
__author__ = 'Naze-'

from datetime import timedelta
import os

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

from Trade.models import BtcValue, Average
from django.db.models import F


# -------------------------------------------------------------------------------------------------------------------- #

add = 0
month = 0
day = 0

for rate in BtcValue.objects.filter(BtcValue.rate)[:43200]:

    add = add + rate.object

mont = add/43200
Average.monthAverage = month
add=0

for rate in BtcValue.objects.filter(BtcValue.rate)[:1440]:

     add = add + rate.object

day = add/1440
Average.dayAverage = day