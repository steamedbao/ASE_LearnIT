from django.contrib import admin
from forum.models import Category, Question, Reply


admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Reply)
