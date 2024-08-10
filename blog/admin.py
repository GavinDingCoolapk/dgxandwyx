from django.contrib import admin

from .models import Post, Wish, Website

# Register your models here.

admin.site.register(Post)
admin.site.register(Wish)
admin.site.register(Website)
