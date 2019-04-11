from django.db import models


class Category(models.Model):
	title = models.CharField(max_length=100)
	icon = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.title}"

class Discovery(models.Model):
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=150)
	channel_name = models.CharField(max_length=100)
	thumbnail = models.ImageField(upload_to = 'media/thumbnails', default = '')
	description = models.TextField()
	votes = models.IntegerField()
	topic = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.title}"
