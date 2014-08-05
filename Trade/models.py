from django.db import models
from decimal import Decimal

# Create your models here.
# -------------------------------------------------------------------------------------------------------------------- #
# python manage.py schemamigration Trade --auto
# python manage.py migrate Trade
# -------------------------------------------------------------------------------------------------------------------- #


class BtcRate(models.Model):
    rate = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    high = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    low = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    ask = models.DecimalField(unique=False, blank=False, max_digits=8, decimal_places=2)
    volume = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8)
    date = models.DateTimeField(unique=False, blank=False, auto_now_add=True)
