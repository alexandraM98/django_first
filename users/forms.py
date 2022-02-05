from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from post.models import TwitterImage


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta: 
		model = User
		fields = ['username', 'email', 'password1', 'password2']

#The UserUpdateForm will allow users to update their username and email
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta: 
		model = User
		fields = ['username', 'email']

#The ProfileUpdateForm will allow users to update their profile picture
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']


class TwitterImageForm(forms.ModelForm):
	class Meta:
		model = TwitterImage
		fields = ['image']