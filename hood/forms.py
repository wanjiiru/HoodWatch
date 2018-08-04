from django import forms
from.models import Neighbourhood,Post,Profile, Business
from django.contrib.auth.forms import AuthenticationForm

class BusinessForm(forms.ModelForm):
    class Meta:
        model  = Business
        fields = ['name','hood']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','bio']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post','user']
