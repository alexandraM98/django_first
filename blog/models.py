from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Each class is going to be its' own table in the database. The Post class below is going to be a database table.
class Post(models.Model): 
	#Creating attributes...
	#Each attribute below will be a field in its' own database
	title = models.CharField(max_length=100)
	content = models.TextField()
	#date_posted = models.DateTimeField(auto_now_add=True) #this will set the "date posted" to the current date time only when this object is created
	#if I want to be able to change the date posted (which isn't possible with auto_now or auto_now_add) we need to import a django utility for a different argument that we want to pass into that function
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE) #If a user is deleted, their posts will also be deleted.

	#After creating this Post model. I must go to the command prompt, cd to my project directory, and enter the command "python manage.py makemigrations".
	#The following message will be displayed "-Create model Post" meaning that the model for a blog post was successfully created.
	#It is possible to see what got created after running that command inside the migrations folder of my app in a file titled "0001_initial.py"

	#Running the command "python manage.py sqlmigrate blog 0001" will display the sql commands written to create that table in the database.

	#This is what Object-Relational-Mapping (ORM) is good for. We don't have to get our hands "dirty" with writing the SQL commands.

	#To make the changes take effect on the actual database, I must run the "python manage.py migrate" command.

	def __str__(self):
		return self.title