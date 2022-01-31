"""djangoFirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from post import views
from django.conf import settings
from django.conf.urls.static import static


#Setting my urls for different views. Admin is a default one, which I am keeping to manage the app.
#I used three different ways of setting views. 
#1. Creating a separate urls.py file inside my blog app and then including that here e.g., the last path in the list below
#2. Creating two functions in the views.py file of my users app, then importing these functions. E.g., when a user navigates to 'register/', the register function of the views.py inside users is accessed.
#3. Importing the authentication views, then setting them to the template that I created (to replace the defaults).

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'), 
    path('profile/', user_views.profile, name='profile'), 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
    path('post/', views.index, name="index")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)