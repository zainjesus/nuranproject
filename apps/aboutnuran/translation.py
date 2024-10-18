from modeltranslation.translator import register, TranslationOptions
from .models import AboutCompany


@register(AboutCompany)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('aboutCompany', 'aboutProject')
    required_languages = ('ru', 'en', 'ky')
