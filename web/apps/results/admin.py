# Django core
from django.contrib import admin

# Models
from .models import (ChoiceBlockResult, FloatBlockResult, Result,
                     TextAnswerBlockResult, TextBlockResult)

# Core django admin site register
admin.site.register(Result)
admin.site.register(TextBlockResult)
admin.site.register(ChoiceBlockResult)
admin.site.register(FloatBlockResult)
admin.site.register(TextAnswerBlockResult)
