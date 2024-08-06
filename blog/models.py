from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    c_cat = [("Recent events", "Recent events"),
             ("Future plans", "Future plans"),
             ("Our memoires", "Our memories"),
             ]

    c_auth = [("Gavin", "Gavin"), ("Asinia", "Asinia")]

    category = models.CharField(choices=c_cat, max_length=50, default="Recent events")
    title = models.CharField(max_length=150)
    date = models.DateField(default=timezone.now)
    author = models.CharField(max_length=15, choices=c_auth, default="Gavin")
    body = models.TextField()
    image = models.ImageField(upload_to='blog/posts/%Y/%m/%d', blank=True)
    tag1 = models.CharField(max_length=15, blank=True)
    tag2 = models.CharField(max_length=15, blank=True)
    tag3 = models.CharField(max_length=15, blank=True)
