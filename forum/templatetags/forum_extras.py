from django import template
from forum.models import Category

register = template.Library()

@register.inclusion_tag('forum/_categories.html')
def show_categories():
    categories = Category.objects.all()
    return { 'categories': categories}
