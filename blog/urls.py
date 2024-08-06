from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('latest_posts', views.latest_posts, name='latest_posts'),
    re_path('search', views.search_posts, name='search_posts'),
    re_path('latest_post_([1-9]+)', views.latest_post, name='spec_latest_post'),
    re_path('post_([0-9]+)', views.spec_post, name='spec_post'),
    re_path('category/(.+)', views.spec_category, name='spec_category'),
    re_path('tag/(.+)', views.spec_tag, name='spec_tag'),
]
