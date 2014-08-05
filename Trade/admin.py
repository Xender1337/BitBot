from django.contrib import admin
from Trade.models import BtcRate, EurUsd, BitstampUser, Average


class BtcRateAdmin(admin.ModelAdmin):
    list_display = ('rate', 'high', 'low', 'ask', 'volume', 'date')
admin.site.register(BtcRate, BtcRateAdmin)


class EurUsdAdmin(admin.ModelAdmin):
    list_display = ('buy', 'sell', 'date')
admin.site.register(EurUsd, EurUsdAdmin)


class BitstampUserAdmin(admin.ModelAdmin):
    list_display = ('UserAccount', 'ApiKey')
admin.site.register(BitstampUser, BitstampUserAdmin)


class AverageAdmin(admin.ModelAdmin):
    list_display = ('monthAverage', 'dayAverage')
admin.site.register(Average, AverageAdmin)