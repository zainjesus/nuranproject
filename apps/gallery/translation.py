from modeltranslation.translator import register, TranslationOptions
from .models import Gallery


@register(Gallery)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('description', )
    required_languages = ('ru', 'en', 'ky')
