from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# The default user model that django provides does not provide a field for the profile picture.
# I must extend that User model and add this feature.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	#we are going to overwrite the default save method
	def save(self, *args, **kwargs):
		super().save()

		img = Image.open(self.image.path)

		if (img.height > 300 or img.width > 300):
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

