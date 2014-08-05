#!/usr/bin/env python
__author__ = 'Naze-'

from datetime import timedelta
import os

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

from Trade.models import BtcValue, Average

# -------------------------------------------------------------------------------------------------------------------- #


add = 0
print "Init"

for value in BtcValue.objects.all()[:43200]:
    print "toto"
    add += value.rate
    print add

month = add/43200
add = 0

for value in BtcValue.objects.all()[:1440]:

     add += value.rate

day = add/1440

Average(monthAverage=month, dayAverage=day).save()