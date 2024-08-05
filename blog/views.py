from django.shortcuts import render, HttpResponse
from blog import models
# Create your views here.


def index(request):
    post1 = models.Post.objects.order_by("-id")[0]
    post2 = models.Post.objects.order_by("-id")[1]
    if post1.image:
        post1_image = "media/" + post1.image.url
    else:
        post1_image = ""
    if post2.image:
        post2_image = "media/" + post2.image.url
    else:
        post2_image = ""
    posts_info = {"post1_title": post1.title,
                  "post1_image": post1_image,
                  "post2_title": post2.title,
                  "post2_image": post2_image,
                  }
    return render(request, "index.html", posts_info)


def about(request):
    return render(request, "about.html")


def latest_post_1(request):
    post = models.Post.objects.order_by("-id")[0]
    post_info = {"category": post.category,
                 "title": post.title,
                 "date": post.date,
                 "author": post.author,
                 "body": post.body.split("\n"),
                 "image": post.image,
                 }
    if post.image:
        post_info["image"] = "media/" + post.image.url
    else:
        post_info["image"] = ""
    return render(request, "post-style-1.html", post_info)


def latest_post_2(request):
    post = models.Post.objects.order_by("-id")[1]
    post_info = {"category": post.category,
                 "title": post.title,
                 "date": post.date,
                 "author": post.author,
                 "body": post.body.split("\n"),
                 "image": post.image,
                 }
    if post.image:
        post_info["image"] = "media/" + post.image.url
    else:
        post_info["image"] = ""
    return render(request, "post-style-1.html", post_info)


def our_memories(request):
    return HttpResponse("this is the Our Memories page")


def our_future(request):
    return HttpResponse("this is the Our Future page")
