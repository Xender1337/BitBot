#!/usr/bin/env python
__author__ = 'Naze-'

from datetime import timedelta
import os

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

from Trade.models import BtcValue, Average
from django.db.models import F


# -------------------------------------------------------------------------------------------------------------------- #

month = 0
day = 0

for rate in BtcValue.objects.filter((mod_date__gt=F('date')) + timedelta(days=30)):

    month = month + rate.object

Average.monthAverage = month

for rate in BtcValue.objects.filter :

     day = day + rate.object

Average.dayAverage = day