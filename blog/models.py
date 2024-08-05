from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    c_cat = [("Recent events", "Recent events"),
             ("Future plans", "Future plans"),
             ("Our memoires", "Our memories"),
             ]

    c_auth = [("Gavin", "Gavin"), ("Asinia", "Asinia")]

    c_style = [(1, "1"),
               (2, "2"),
               (3, "3"),
               (4, "4"),
               (5, "5"),
               (6, "6"),
               (7, "7"),
               (8, "8"),
               (9, "9"),
               (10, "10"),
               (11, "11"),
               ]

    category = models.CharField(choices=c_cat, max_length=50, default="Recent events")
    title = models.CharField(max_length=150)
    date = models.DateField(default=timezone.now)
    author = models.CharField(max_length=15, choices=c_auth, default="Gavin")
    body = models.TextField()
    image = models.ImageField(upload_to='blog/posts/%Y/%m/%d', blank=True)
    tag1 = models.CharField(max_length=15, blank=True)
    tag2 = models.CharField(max_length=15, blank=True)
    tag3 = models.CharField(max_length=15, blank=True)
    post_style = models.IntegerField(choices=c_style, default=1)
