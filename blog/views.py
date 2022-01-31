from django.shortcuts import render 
from .models import Post

#Posts dummy data to test the app
#posts = [
#	{
#		'author' : 'CoreyMS',
#		'title' : 'Blog Post 1',
#		'content' : 'First Post content',
#		'date_posted' : 'August 27, 2018'
#	},
#	{
#		'author' : 'Alex M',
#		'title' : 'Blog Post 2',
#		'content' : 'Second Post content',
#		'date_posted' : 'August 28, 2018'
#	}
#]


def home(request):
	#we can pass the dummy posts into our template just by passing an argument with our data (inside a dictionary)
	context = {
	#   key      value
		'posts': Post.objects.all()
	}
	#adding this dictionary as a 3rd argument will allow me to pass the dictionary into the template so that I can access it from within the template
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})

