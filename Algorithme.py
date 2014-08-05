#!/usr/bin/env python
__author__ = 'Naze'

from datetime import timedelta
import os

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

from Trade.models import BtcValue, Average
from django.db.models import F


# -------------------------------------------------------------------------------------------------------------------- #

current_rate = BtcValue.objects.filter[:1]

if current_rate < Average.object.filter(Average.monthAverage)[:1] && current_rate < Average.objects.filter(Average.dayAverage)[:1]:
    achat()

def achat():
