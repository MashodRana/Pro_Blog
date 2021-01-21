from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUserModel


class CustomUserCreationForm(UserCreationForm):
    """ Form for user creation """

    class Meta(UserCreationForm.Meta):
        model = CustomUserModel
        fields = ('username', 'email', 'age', 'profession')


class CustomUserChangeForm(UserChangeForm):
    """ Form for changing user information """

    class Meta:
        model = CustomUserModel
        fields = ('username', 'email', 'age', 'profession')
        


