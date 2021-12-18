from django.contrib import admin
from django.contrib.admin import ModelAdmin

from advertisements.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(ModelAdmin):
    pass

