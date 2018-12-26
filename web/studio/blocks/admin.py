# Django core
from django import forms
from django.contrib import admin

# Third-party
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import MarkdownxWidget

# Other apps
from custom_admin.admin import custom_admin

# Models
from .models import (Block, ChoiceBlock, ChoiceBlockOption, FloatBlock,
                     TextAnswerBlock, TextBlock)


# Module for adding choices directly from editing choice_block instance
class ChoiceBlockOptionInline(admin.TabularInline):
    model = ChoiceBlockOption
    extra = 4


class ChoiceBlockAdmin(admin.ModelAdmin):
    inlines = [ChoiceBlockOptionInline]


# Customize default markdownx widget with two-column template
class CustomMarkdownxWidget(MarkdownxWidget):
    template_name = 'blocks/widgets/body.html'


class TextBlockAdminForm(forms.ModelForm):
    class Meta:
        model = TextBlock
        fields = '__all__'
        widgets = {
            'body': CustomMarkdownxWidget
        }


# TODO: add two columns layout for markdownx
# TODO: enable auto updating by MathJax
# Add MathJax javascript to admin page for pre-rendering
class TextBlockAdmin(MarkdownxModelAdmin):

    class Media:
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML',
        )
    # custom 2-columns form try
    # form = TextBlockAdminForm


# Core django admin site register
admin.site.register(Block)
admin.site.register(TextBlock, TextBlockAdmin)
admin.site.register(ChoiceBlock, ChoiceBlockAdmin)
admin.site.register(FloatBlock)
admin.site.register(TextAnswerBlock)

# Custom_Admin site register
custom_admin.register(TextBlock, TextBlockAdmin)
