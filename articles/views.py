from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model

from .models import ArticleModel, CommentModel
from .forms import ArticleForm, CommentForm
# Create your views here.



#-------------------------------------------------------#
#                   Article Views                       #
#-------------------------------------------------------#

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
    # fields = ['title', 'body'] # Fields will be written
    form_class = ArticleForm
    login_url = 'login' # Since login is required

    def form_valid(self, form):
        """ Initialize the logged in user as the article author """
        form.instance.article_writer = self.request.user
        return super().form_valid(form)
    


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """ Control article information editing """

    login_url = 'login'

    model = ArticleModel
    form_class = ArticleForm
    template_name = 'new_article.html'
    # fields = ('title', 'body')

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


class DraftArticleView(LoginRequiredMixin, ListView):
    """ Fetch all the draft articles """
    
    login_url = 'login'
    
    model = ArticleModel
    template_name = 'draft_articles.html'
    context_object_name = 'draft_articles'

    def get_queryset(self):
        return ArticleModel.objects.filter(article_writer=self.request.user).order_by('created_date')


#-------------------------------------------------------#
#                   Comment Views                       #
#-------------------------------------------------------#




#--------------------------------------------------------------#
                # FUNCTIONAL VIEWS #
#--------------------------------------------------------------#

@login_required
def add_comment_view(request, pk):
    article = get_object_or_404(ArticleModel, pk=pk)

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.comment_writer = request.user
            comment.save()
            return redirect('detail_article', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form':form})




@login_required
def change_status_view(request, pk, val):
    print(pk)
    print(val)
    article = get_object_or_404(ArticleModel, pk=pk)
    if val:
        article.article_status(status=True)
    else:
        article.article_status(status=False)

    return redirect('detail_article', pk=article.pk)



    



