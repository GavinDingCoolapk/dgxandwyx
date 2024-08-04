from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def our_memories(request):
    return HttpResponse("this is the Our Memories page")


def our_future(request):
    return HttpResponse("this is the Our Future page")
