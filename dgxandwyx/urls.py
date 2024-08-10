"""dgxandwyx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', views.index, name='index'),
    path('blog/', include('blog.urls')),
    path('best_wishes', views.best_wishes, name='best_wishes'),
    path('wishes_sent', views.send_wishes, name='send_wishes'),
    path('collections', views.collections, name='collections'),
    path('about', views.about, name='about'),
]
