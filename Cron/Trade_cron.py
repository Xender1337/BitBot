#!/usr/bin/env python

# -------------------------------------------------------------------------------------------------------------------- #

__author__ = 'Xender'
# -------------------------------------------------------------------------------------------------------------------- #


### IMPORT
import BitstampAPI
import os
import datetime
# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BitBot.settings")

### SCRIPT
print datetime.datetime.now()

API = BitstampAPI.API()

info = API.GetRate()
