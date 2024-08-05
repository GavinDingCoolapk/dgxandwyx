from django.shortcuts import render, HttpResponse
from blog import models
# Create your views here.


def index(request):
    posts = models.Post.objects.all()
    post1 = posts[0]
    post2 = posts[1]
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


def latest_post(request):
    post = models.Post.objects.get()
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
