#!/usr/bin/env python
__author__ = 'Naze-'

import datetime
from datetime import timedelta
import os

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

from Trade.models import BtcValue, Average

# -------------------------------------------------------------------------------------------------------------------- #

cnt = 0
add = 0
now = datetime.datetime.now()
td = timedelta(days=-30)
date = now - td

print "Init"

for value in BtcValue.objects.filter(date):
    cnt += 1
    add += value.rate
    print add

month = add/cnt
add = 0
cnt = 0
for value in BtcValue.objects.all()[:1440]:
    cnt += 1
    add += value.rate

day = add/1440

Average(monthAverage=month, dayAverage=day).save()