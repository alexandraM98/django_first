from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

#to make the styling of forms easier, there is a third party tool called crispy forms which will help generate Bootstrap-like forms.
#Creating forms from scratch would mean a lot of processing and validation.
	#Django takes care of a lot of this from the backend.
	#Python classes can be created and these classes generate HTML forms for developers. Some of these classes already exist, but I can also create my own.

def register(request):
	if (request.method == 'POST'):
		form = UserRegisterForm(request.POST) #if the form method is POST then we instantiate a user creation form with that post request data
		if form.is_valid():
			form.save() #this is all that's needed to save the user to the database
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created. You are now able to log in.')
			return redirect('login')
	else:
		form = UserRegisterForm() #with any other request, it just instantiates an empty form
	return render(request, 'users/register.html', {'form' : form})


@login_required #this decorator adds functionality to an existing function. In this case, it adds functionality to my profile view where the user must be logged in to view this page.
def profile(request):
	return render(request, 'users/profile.html')

#Types of messages:
#messages.debug
#messages.info
#messages.success
#messages.error