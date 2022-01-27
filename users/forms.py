from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'nickname', 'avatar', 'age', 'level', 'first_name',
                  'last_name', 'last_login', 'location')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'nickname', 'avatar', 'age', 'level', 'first_name',
                  'last_name', 'last_login', 'location')












