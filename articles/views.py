from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ArticleModel
from .forms import ArticleForm


# Create your views here.
class Home(ListView):
    """ Control all the articles viewing on the template """

    model = ArticleModel
    template_name = 'home.html'
    context_object_name = 'all_article'

    def get_queryset(self):
        return ArticleModel.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class ArticleDetailView(LoginRequiredMixin, DetailView):
    """ Control view of an article information """

    login_url = 'login'

    model = ArticleModel
    template_name = 'detail_article.html'
    context_object_name = 'article'



class ArticleCreateView(LoginRequiredMixin, CreateView):
    """ Control article creation """
    model = ArticleModel # where aricle information will be saved.
    template_name = 'new_article.html' # Which html file will be used for article creation.
    fields = ['title', 'body'] # Fields will be written
    # form_class = ArticleForm
    login_url = 'login' # Since login is required

    def form_valid(self, form):
        """ Initialize the logged in user as the article author """
        form.instance.article_writer = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """ Control article information editing """

    login_url = 'login'

    model = ArticleModel
    template_name = 'edit_article.html'
    fields = ('title', 'body')

    def dispatch(self, request, *args, **kwargs):
        """ Make sure that no one can update/edit an article except the original writter. """

        _object = self.get_object()

        if _object.article_writer != request.user:
            # Logged user is not the writer of the article.
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)



class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """ control an article deleting form the tabel/model """

    login_url = 'login'

    model = ArticleModel
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')
    context_object_name = 'article'

    def dispatch(self, request, *args, **kwargs):
        """ Make sure that no one can delete an article except the original writter. """

        _object = self.get_object()

        if _object.article_writer != request.user:
            # Logged user is not the writer of the article.
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)





