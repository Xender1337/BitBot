from django.contrib import admin
from django.forms import ModelForm, PasswordInput
from Trade.models import BtcValue, EurUsd, BitstampUser, Average, AlgOption, Order


class BtcValueAdmin(admin.ModelAdmin):
    list_display = ('rate', 'high', 'low', 'ask', 'volume', 'date')
admin.site.register(BtcValue, BtcValueAdmin)


class EurUsdAdmin(admin.ModelAdmin):
    list_display = ('buy', 'sell', 'date')
admin.site.register(EurUsd, EurUsdAdmin)


class BitstampUserAdmin(admin.ModelAdmin):
    list_display = ('AccountName', 'UserID',
                    'PublicKey', 'BtcBalance',
                    'UsdBalance', 'Fee',
                    'account_value_btc', 'account_value_usd')
admin.site.register(BitstampUser, BitstampUserAdmin)


class AverageAdmin(admin.ModelAdmin):
    list_display = ('monthAverage', 'dayAverage')
admin.site.register(Average, AverageAdmin)


class AlgOptionAdmin(admin.ModelAdmin):
    list_display = ('Status', 'BuyRate', 'cpt', 'date')
admin.site.register(AlgOption, AlgOptionAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('BitstampUser', 'OrderId', 'Price', 'Amount', 'RequestType', 'OrderType', 'Status')
admin.site.register(Order, OrderAdmin)