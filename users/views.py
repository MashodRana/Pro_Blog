from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied

from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm, CustomLoginForm, CustomUserChangeForm
from .models import CustomUserModel


# Create your views here.
class SignupView(CreateView):
    """ Control signup functionality """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CustomLoginView(LoginView):

    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
    authentication_form = CustomLoginForm


class UserUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile')
    form_class = CustomUserChangeForm
    model = CustomUserModel

    def dispatch(self, request, *args, **kwargs):
        """ Make sure that no one can update/edit others profile informations. """

        _object = self.get_object()

        if _object.pk != request.user.pk:
            # Logged user is not the writer of the article.
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)



