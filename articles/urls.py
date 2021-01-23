from django.urls import path
from django.views.generic import TemplateView

from articles import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about' ),
    path('article/new/', views.ArticleCreateView.as_view(), name='new_article'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='edit_article'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name = 'delete_article'),
    path('article/<int:pk>/detail/', views.ArticleDetailView.as_view(), name = 'detail_article'),
    path('article/drafts/', views.DraftArticleView.as_view(), name = 'draft_articles'),
    path('article/<int:pk>/change_status/<int:val>', views.change_status_view, name = 'change_status'),
    path('article/<int:pk>/comment/',views.add_comment_view, name='add_comment'),
    
]