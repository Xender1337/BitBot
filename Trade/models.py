from django.db import models
from decimal import Decimal

# -------------------------------------------------------------------------------------------------------------------- #
# python manage.py schemamigration Trade --auto
# python manage.py migrate Trade
# -------------------------------------------------------------------------------------------------------------------- #

from datetime import datetime

class BtcValue(models.Model):
    rate = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    high = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    low = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    ask = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    volume = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8)
    date = models.DateTimeField(unique=False, blank=False, auto_now_add=True)


class Average(models.Model):
    monthAverage = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8)
    dayAverage = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8)


class EurUsd(models.Model):
    buy = models.DecimalField(unique=False, blank=False, max_digits=5, decimal_places=4)
    sell = models.DecimalField(unique=False, blank=False, max_digits=5, decimal_places=4)
    date = models.DateTimeField(unique=False, blank=False, auto_now_add=True)


class BitstampUser(models.Model):
    AccountName = models.CharField(unique=True, blank=False, max_length=100)
    UserID = models.IntegerField(unique=True, blank=False, max_length=10)
    PublicKey = models.CharField(unique=True, blank=False, max_length=255)
    SecretKey = models.CharField(unique=True, blank=False, max_length=255)
    BtcBalance = models.DecimalField(unique=False, max_digits=10, decimal_places=8, default=0)
    UsdBalance = models.DecimalField(unique=False, max_digits=16, decimal_places=2, default=0)
    BtcAvailable = models.DecimalField(unique=False, max_digits=10, decimal_places=8, default=0)
    UsdAvailable = models.DecimalField(unique=False, max_digits=16, decimal_places=2, default=0)
    BtcReserved = models.DecimalField(unique=False, max_digits=10, decimal_places=8, default=0)
    UsdReserved = models.DecimalField(unique=False, max_digits=16, decimal_places=2, default=0)
    BtcTotal = models.DecimalField(unique=False, max_digits=10, decimal_places=8, default=0)
    UsdTotal = models.DecimalField(unique=False, max_digits=16, decimal_places=2, default=0)
    Fee = models.DecimalField(unique=False, max_digits=3, decimal_places=2, default=0.05)

    @property
    def account_value_btc(self):
        total = self.BtcBalance + self.BtcAvailable + self.BtcReserved
        return total

    @property
    def account_value_usd(self):
        total = self.UsdAvailable + self.UsdBalance + self.UsdReserved
        return total

    def __unicode__(self):
        return "Account : " + self.AccountName + " // UserID : " + str(self.UserID)

class AlgOption(models.Model):
    Status = models.IntegerField(unique=True, blank=False, max_length=2)
    BuyRate = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8)
    cpt = models.IntegerField(unique=True, blank=False, max_length=2)
    date = models.DateTimeField(unique=False, blank=False)
