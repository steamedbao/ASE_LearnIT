from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from ..forms import ReplyForm
from ..models import Question, Reply


# class based views
class IndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        if 'q' in self.request.GET:
            search = self.request.GET['q']

            return Question.objects.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )
        else:
            return reversed(get_list_or_404(Question))


class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'questions/question_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplyForm

        return context

    def post(self, request, *args, **kwargs):
        form = ReplyForm(request.POST)

        if form.is_valid():
            reply = form.save(commit=False)
            reply.creator = request.user
            reply.question = self.get_object()
            reply.save()

            self.object = self.get_object()

            context = context = super().get_context_data(**kwargs)
            context['form'] = ReplyForm

            return self.render_to_response(context=context)

        else:
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = form

            return self.render_to_response(context=context)


class QuestionUpdateView(generic.UpdateView):
    model = Question
    fields = ['category', 'content']
    template_name = 'questions/update_question.html'


class QuestionCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = '/accounts/login'
    model = Question
    template_name = 'questions/new_question.html'
    fields = ['category', 'title', 'content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class QuestionDeleteView(generic.edit.DeleteView):
    model = Question
    success_url = reverse_lazy('index')


def like_or_dislike_question(request, id):
    question = get_object_or_404(Question, pk=id)
    current_user = request.user

    if question.is_liked_by(current_user):
        question.dislike(current_user)
        return JsonResponse({'message': 'disliked'})

    question.like(current_user)
    return JsonResponse({'message': 'liked'})
