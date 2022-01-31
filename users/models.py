from django.db import models
from django.contrib.auth.models import User

# The default user model that django provides does not provide a field for the profile picture.
# I must extend that User model and add this feature.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'