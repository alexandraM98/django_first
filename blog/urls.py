from django.urls import path
#importing the function from the views.py file; where '.' is our current directory
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/ ', views.about, name='blog-about'),
]