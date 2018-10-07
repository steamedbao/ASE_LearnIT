from django import template

from questions.models import Category

register = template.Library()


@register.inclusion_tag('questions/_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
