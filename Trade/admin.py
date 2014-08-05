from django.contrib import admin
from Trade.models import BtcRate

# Register your models here.


class BtcRateAdmin(admin.ModelAdmin):
    list_display = ('rate', 'high', 'low', 'ask', 'volume', 'date')

admin.site.register(BtcRate, BtcRateAdmin)