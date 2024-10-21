from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Gallery, Stages


@admin.register(Gallery)
class AboutCompanyAdmin(TranslationAdmin):
    list_display = ('description', )

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    


@admin.register(Stages)
class StagesAdmin(admin.ModelAdmin):
    list_display = ('image',)

