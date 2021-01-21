from django.urls import path

from articles import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('article/new/', views.ArticleCreateView.as_view(), name='new_article'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='edit_article'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name = 'delete_article'),
    path('article/<int:pk>/detail/', views.ArticleDetailView.as_view(), name = 'detail_article'),
    
]