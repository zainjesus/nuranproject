from django.contrib import admin
from .models import Order, Email


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'number',)
    search_fields = ('name', 'number',)


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', )
