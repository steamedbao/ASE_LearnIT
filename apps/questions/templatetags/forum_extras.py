from hashlib import md5

from django import template
from django.contrib.auth.models import User

from apps.questions.models import Category, Question, Reply

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


@register.simple_tag
def total_members_count():
    return User.objects.all().count()


@register.simple_tag
def total_questions_count():
    return Question.objects.all().count()


@register.simple_tag
def total_replies_count():
    return Reply.objects.all().count()


@register.filter(name='gravatar')
def gravatar(user, size=35):
    email = str(user.email.strip().lower()).encode('utf-8')
    email_hash = md5(email).hexdigest()
    url = "//www.gravatar.com/avatar/{0}?s={1}&d=identicon&r=PG"
    return url.format(email_hash, size)
