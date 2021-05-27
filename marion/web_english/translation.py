from modeltranslation.translator import register, TranslationOptions
from .models import Blog,Head_titel

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('titel','post')
@register(Head_titel)
class Head_titelTranslationOptions(TranslationOptions):
    fields = ('titel','subtitel')