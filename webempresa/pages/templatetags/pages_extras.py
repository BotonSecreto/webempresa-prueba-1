from django import template
from pages.models import Page

# registrando en la librería de Templates
register = template.Library()

#El tag devolverá una lista de páginas
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages