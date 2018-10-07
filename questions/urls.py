from django.urls import path

from .views import (CategoryDetailView, QuestionCreateView, QuestionDeleteView,
                    QuestionDetailView, QuestionUpdateView, ReplyDeleteView,
                    ReplyUpdateView)

urlpatterns = [
    path('categories/<slug:slug>', CategoryDetailView.as_view(), name='category'),

    path('new', QuestionCreateView.as_view(), name='new_question'),
    path('categories/<slug:slug>', CategoryDetailView.as_view(), name='category'),
    path('<slug:slug>/edit', QuestionUpdateView.as_view(), name='update_question'),
    path('new', QuestionCreateView.as_view(), name='new_question'),
    path('<slug:slug>', QuestionDetailView.as_view(), name='question'),
    path('<slug:slug>/edit', QuestionUpdateView.as_view(), name='update_question'),
    path('<slug:slug>/delete', QuestionDeleteView.as_view(), name='delete_question'),

    path('<slug:slug>/replies/<int:pk>/edit',
         ReplyUpdateView.as_view(), name='update_reply'),
    path('<slug:slug>/replies/<int:pk>/delete',
         ReplyDeleteView.as_view(), name='delete_reply'),
]
