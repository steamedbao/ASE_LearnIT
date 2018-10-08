from django import template

from apps.questions.models import Category

register = template.Library()


@register.inclusion_tag('questions/_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}


@register.simple_tag
def reply_liked_by(reply, user):
    return reply.is_liked_by(user)


@register.simple_tag
def question_liked_by(question, user):
    return question.is_liked_by(user)
