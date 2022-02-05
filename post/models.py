from django.db import models

class TwitterImage(models.Model):
	image = models.ImageField(default='default.jpg', upload_to='post')

	def __str__(self):
		return self.image


