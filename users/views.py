from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


# Create your views here.
class SignupView(CreateView):
    """ Control signup functionality """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


