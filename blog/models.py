from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

	title = models.CharField(max_length =100)
	content = models.TextField()
	date_posted = models.DateTimeField(default =timezone.now) #saves the posted time and can be changed later
	author = models.ForeignKey(User, on_delete = models.CASCADE) #deletes the posts of deleted user

	def __str__(self):          #this method helps to add more detail (title) in Post.objects.all() function in django shell
		return self.title