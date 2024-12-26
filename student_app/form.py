from django.forms import ModelForm
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "about", "pub_date"]
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
