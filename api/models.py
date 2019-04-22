from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Category(models.Model):
	title = models.CharField(max_length=100)
	icon = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.title}"


class Discovery(models.Model):
	title = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now_add = True)
	url = models.CharField(max_length=150)
	channel_name = models.CharField(max_length=100)
	thumbnail = models.CharField(max_length=150, blank=True, null=False)
	embed = models.CharField(max_length=200, blank=True, null=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()
	votes = models.IntegerField(default=0)
	categories = ArrayField(models.IntegerField(blank=True, null=True), blank=True)

	@property
	def categories_obj(self):
		objs = []
		for pk in self.categories:
			obj = Category.objects.get(pk=pk)
			objs.append(obj)
		return objs

	@property
	def comments(self):
		comments = Comments.objects.filter(discovery=self)
		return list(comments)	


	def __str__(self):
		return f"{self.title}"

class Comments(models.Model):
	comment = models.CharField(max_length=100)
	discovery = models.ForeignKey(Discovery, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return f"{self.user}"


 
