from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

User = get_user_model()

class UpdateProfileForm(ModelForm):
    UserID = Profile.UserID
    SelectedCity = Profile.SelectedCity
    class Meta:
        model = Profile
        fields = ['UserID','SelectedCity']

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")