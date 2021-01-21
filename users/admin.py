from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUserModel
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
    """ Customizing Admin user """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    list_display = ['email', 'username', 'age', 'profession', 'is_staff']


admin.site.register(CustomUserModel, CustomUserAdmin)

