#!/usr/bin/env python
__author__ = 'Naze-'

from datetime import timedelta, datetime
import os

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")
from Trade.models import BtcValue, Average

# -------------------------------------------------------------------------------------------------------------------- #

cnt = 0
add = 0

print "Init"

for value in BtcValue.objects.filter(date__gte=datetime.now()-timedelta(days=30)):
    cnt += 1
    add += value.rate

month = add/cnt
print "month :" + str(month)

add = 0
cnt = 0
for value in BtcValue.objects.filter(date__gte=datetime.now()-timedelta(days=1)):
    cnt += 1
    add += value.rate

day = add/cnt
print 'day :' + str(day)

Average(monthAverage=month, dayAverage=day).save()