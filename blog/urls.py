from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('posts',views.posts,name="all-posts"),
    path('posts/<str:slug>/<int:id>',views.single_post,name="single-post"),
    path('tag/<str:tag_name>',views.tag_posts, name="tag-posts"),
    path('author/posts/<int:id>/',views.author_posts, name="author-posts")
]