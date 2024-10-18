from django.contrib import admin
from .models import Gallery, Stages

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Stages)
class StagesAdmin(admin.ModelAdmin):
    list_display = ('image',)

