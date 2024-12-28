from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('posts', views.Posts.as_view(), name="all-posts"),
    path('posts/add-post', views.AddPost.as_view(), name="add-post"),
    path('posts/add-comment/<int:id>',views.AddComment.as_view(),name="add-comment"),
    path('posts/<str:slug>/<int:id>', views.SinglePost.as_view(), name="single-post"),
    path('tag/<str:tag_name>', views.TagPosts.as_view(), name="tag-posts"),
    path('author/posts/<int:id>', views.AuthorPosts.as_view(), name="author-posts"),
    path('read-later',views.ReadLater.as_view(),name="read-later")
]
