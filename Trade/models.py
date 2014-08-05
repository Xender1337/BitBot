from django.db import models
from decimal import Decimal

# -------------------------------------------------------------------------------------------------------------------- #
# python manage.py schemamigration Trade --auto
# python manage.py migrate Trade
# -------------------------------------------------------------------------------------------------------------------- #


class BtcValue(models.Model):
    rate = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    high = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    low = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    ask = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    volume = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8)
    date = models.DateTimeField(unique=False, blank=False, auto_now_add=False)


class Average(models.Model):
    monthAverage = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8)
    dayAverage = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8)


class EurUsd(models.Model):
    buy = models.DecimalField(unique=False, blank=False, max_digits=5, decimal_places=4)
    sell = models.DecimalField(unique=False, blank=False, max_digits=5, decimal_places=4)
    date = models.DateTimeField(unique=False, blank=False, auto_now_add=True)


class BitstampUser(models.Model):
    UserAccount = models.CharField(unique=True, blank=False, max_length=100)
    ApiKey = models.CharField(unique=True, blank=False, max_length=255)

class AlgOption(models.Model):
    Status = models.IntegerField(unique=True, blank=False, max_length=2)
    BuyRate = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8)
    cpt = models.IntegerField(unique=True, blank=False, max_length=2)
