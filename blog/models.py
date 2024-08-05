from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    date = models.DateField(default=timezone.now)
    author = models.CharField(max_length=10)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/posts/%Y/%m/%d', blank=True)
