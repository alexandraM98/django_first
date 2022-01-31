from django.contrib import admin
from .models import Post

# Register your models here.
#To register the models, we need to import the model first

admin.site.register(Post)