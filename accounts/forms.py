from django import forms
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', )
    
class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', )