from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} {self.text}"

class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return f"{self.author} has a comment with text {self.text}"
