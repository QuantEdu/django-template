# Django Core
from django import template
# Third party
from markdownx.utils import markdownify

# pointer to the current instance
register = template.Library()


# Register template tag globally
# it can be add to the tpl by {% load markdownx %}
@register.filter
def show_markdown(text):
    return markdownify(text)
