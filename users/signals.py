from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#we want to get a signal whenever a user is created so that we don't have to manually create a profile for each user. When a user is created, a profile will be created for that user.

@receiver (post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance) #we want to run this everytime a user is created

@receiver (post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save() #we want to run this everytime a user is created

