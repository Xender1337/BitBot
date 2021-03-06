from django.db import models

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
        total = self.BtcAvailable + self.BtcReserved
        return total

    @property
    def account_value_usd(self):
        total = self.UsdAvailable + self.UsdReserved
        return total

    def __unicode__(self):
        return "Account : " + self.AccountName + " // UserID : " + str(self.UserID)


class Order(models.Model):
    TYPE_REQUEST = (
        (0, 'Open Order'),
        (1, 'Cancel Order'),
        (2, 'Buy Limit Order'),
        (3, 'Sell Limit Order')
    )
    TYPE_ORDER = (
        (0, 'Buy'),
        (1, 'Sell')
    )
    TYPE_STATUS = (
        (0, 'Actually'),
        (1, 'Done')
    )
    BitstampUser = models.ForeignKey(BitstampUser)
    OrderId = models.IntegerField(blank=False, unique=True, max_length=20,)
    Price = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8, default=0)
    Amount = models.DecimalField(unique=False, blank=False, max_digits=16, decimal_places=8, default=0)
    RequestType = models.IntegerField(unique=False, blank=False, choices=TYPE_REQUEST)
    OrderType = models.IntegerField(unique=False, blank=False, choices=TYPE_ORDER)
    Status = models.IntegerField(unique=False, blank=False, choices=TYPE_STATUS)


class AlgOption(models.Model):
    Status = models.IntegerField(unique=False, blank=False, max_length=2)
    BuyRate = models.DecimalField(unique=False, blank=False, default=0, max_digits=16, decimal_places=8)
    cpt = models.IntegerField(unique=False, blank=False, max_length=2)
    date = models.DateTimeField(unique=False, blank=False)
