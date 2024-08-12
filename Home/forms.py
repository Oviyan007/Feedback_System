from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile

class RegistrationForm(UserCreationForm):
    DESIGNATION_CHOICES = [
        ('STUDENT', 'Student'),
        ('FACULTY', 'Faculty'),
    ]

    designation = forms.ChoiceField(choices=DESIGNATION_CHOICES, widget=forms.Select)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'designation']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name']


