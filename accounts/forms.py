from django import forms
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model
from allauth.account.forms import (
    SignupForm as BaseSignUpForm,
    LoginForm as BaseLoginForm
)



class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', )
    
class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', )

class LoginForm(BaseLoginForm):
    remember = forms.BooleanField(label=("Remember Me"), required=False, widget=forms.HiddenInput)

class SignUpForm(BaseSignUpForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
