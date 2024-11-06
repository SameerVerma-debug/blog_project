from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('posts',views.posts,name="all-posts"),
    path('posts/<id>',views.single_post,name="single-post")
]
