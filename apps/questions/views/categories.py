from django.views import generic

from ..models import Category


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'questions/category.html'
