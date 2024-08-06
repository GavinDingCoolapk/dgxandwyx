from django.shortcuts import render, HttpResponse
from blog import models
from django.db.models import Q
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
                  "post1_category": post1.category,
                  "post2_title": post2.title,
                  "post2_image": post2_image,
                  "post2_category": post2.category,
                  }
    return render(request, "index.html", posts_info)


def search_posts(request):
    if request.method == "POST":
        key_word = request.POST["key_word"]
        posts = models.Post.objects.filter(title__contains=key_word).order_by("-id")
        posts_info = {"posts": posts,
                      "key_word": key_word,
                      }
        return render(request, "search_posts.html", posts_info)


def latest_posts(request):
    posts = models.Post.objects.order_by("-id")
    posts_info = {"posts": posts}
    return render(request, "latest_posts.html", posts_info)


def latest_post(request, num):
    post = models.Post.objects.order_by("-id")[int(num) - 1]
    post_info = {"category": post.category,
                 "title": post.title,
                 "date": post.date,
                 "author": post.author,
                 "body": post.body.split("\n"),
                 "image": post.image,
                 "tag1": post.tag1,
                 "tag2": post.tag2,
                 "tag3": post.tag3,
                 }
    if post.image:
        post_info["image"] = "media/" + post.image.url
    else:
        post_info["image"] = ""
    return render(request, "post.html", post_info)


def spec_post(request, num):
    post = models.Post.objects.get(id=num)
    post_info = {"category": post.category,
                 "title": post.title,
                 "date": post.date,
                 "author": post.author,
                 "body": post.body.split("\n"),
                 "image": post.image,
                 "tag1": post.tag1,
                 "tag2": post.tag2,
                 "tag3": post.tag3,
                 }
    if post.image:
        post_info["image"] = "media/" + post.image.url
    else:
        post_info["image"] = ""
    return render(request, "post.html", post_info)


def spec_category(request, cat_name):
    posts = models.Post.objects.filter(category=cat_name).order_by("-id")
    posts_info = {"posts": posts,
                  "category": cat_name,
                  }
    return render(request, "category_posts.html", posts_info)


def spec_tag(request, tag_name):
    posts = models.Post.objects.filter(Q(tag1=tag_name) | Q(tag2=tag_name) | Q(tag3=tag_name)).order_by("-id")
    posts_info = {"posts": posts,
                  "tag": tag_name,
                  }
    return render(request, "tag_posts.html", posts_info)


def best_wishes(request):
    return HttpResponse("this is the best wishes page")


def our_collections(request):
    return HttpResponse("this is the our collection page")


def about(request):
    number = {"gavin": len(models.Post.objects.filter(author="Gavin")),
              "asinia": len(models.Post.objects.filter(author="Asinia"))
              }
    return render(request, "about.html", number)
