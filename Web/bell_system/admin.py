# bell_system/admin.py

from django.contrib import admin
from .models import BusRoute, BusStop

class BusStopInline(admin.TabularInline):
    model = BusStop
    extra = 1

class BusRouteAdmin(admin.ModelAdmin):
    inlines = [BusStopInline]

admin.site.register(BusRoute, BusRouteAdmin)
