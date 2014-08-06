from django.contrib import admin
from Trade.models import BtcValue, EurUsd, BitstampUser, Average, AlgOption


class BtcValueAdmin(admin.ModelAdmin):
    list_display = ('rate', 'high', 'low', 'ask', 'volume', 'date')
admin.site.register(BtcValue, BtcValueAdmin)


class EurUsdAdmin(admin.ModelAdmin):
    list_display = ('buy', 'sell', 'date')
admin.site.register(EurUsd, EurUsdAdmin)


class BitstampUserAdmin(admin.ModelAdmin):
    list_display = ('UserAccount', 'ApiKey')
admin.site.register(BitstampUser, BitstampUserAdmin)


class AverageAdmin(admin.ModelAdmin):
    list_display = ('monthAverage', 'dayAverage')
admin.site.register(Average, AverageAdmin)


class AlgOptionAdmin(admin.ModelAdmin):
    list_display = ('Status', 'BuyRate', 'cpt', 'date')
admin.site.register(AlgOption, AlgOptionAdmin)