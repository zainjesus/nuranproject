from django.contrib import admin
from .models import Links


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('yt_link', 'ig_link', 'wt_link', 'email_link')