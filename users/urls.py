from django.urls import path

from users import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('profile/<int:pk>/edit/', views.UserUpdateView.as_view(), name='profile_edit'),
]