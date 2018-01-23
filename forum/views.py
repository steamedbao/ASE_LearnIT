from django.db.models import Q
from django.views import generic
from .models import Category, Question
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, get_list_or_404

class IndexView(generic.ListView):
    template_name = 'forum/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        if 'search' in self.request.GET:
            search = self.request.GET['search']
            return Question.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
                )
        else:
            return reversed(get_list_or_404(Question))


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'forum/category.html'


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'forum/question.html'


class QuestionCreateView(generic.CreateView):
    model = Question
    template_name = 'forum/new_question.html'
    fields = ['category', 'title', 'content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
