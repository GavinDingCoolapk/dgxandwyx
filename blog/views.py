from django.shortcuts import render, HttpResponse
from blog import models
# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def latest_post(request):
    post = models.Post.objects.get(id=1)
    post_info = {"category": post.category,
                 "title": post.title,
                 "date": post.date,
                 "author": post.author,
                 "body": post.body.split("\n"),
                 "para_num": len(post.body.split("\n")) // 2,
                 "image": post.image,
                 }
    return render(request, "post-style-1.html", post_info)


def our_memories(request):
    return HttpResponse("this is the Our Memories page")


def our_future(request):
    return HttpResponse("this is the Our Future page")
