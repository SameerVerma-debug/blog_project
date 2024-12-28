from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from .models import Post, Tag, Author, Comment
from django.views import View
from .forms import AddPostForm,AddCommentForm
from django.urls import reverse

LATEST_POSTS_NUM = 3

# Create your views here.

class Index(View):
    def get(self, request):
        try:
            latest_posts = Post.objects.all().order_by("-date")[:LATEST_POSTS_NUM]

            return render(request, "blog/index.html", {
                "posts": latest_posts
            })
        except:
            return HttpResponseServerError("Something Went Wrong!!")


class Posts(View):
    def get(self, request):
        try:
            all_posts = Post.objects.all()
            return render(request, "blog/posts.html", {
                "posts": all_posts
            })
        except:
            return HttpResponseServerError("Something Went Wrong!!")


class SinglePost(View):
    def get(self, request, slug, id):
        try:
            found_post = Post.objects.get(slug=slug.lower(), id=int(id))
            found_post_tags = found_post.tags.all()
            found_post_comments = found_post.comments.all()
            
            print("----",found_post_comments)
            return render(request, "blog/post.html", {
                "post": found_post,
                "post_tags": found_post_tags,
                "post_comments":found_post_comments
            })
        except:
            raise Http404()


class TagPosts(View):
    def get(self, request, tag_name):
        try:
            tag = Tag.objects.get(caption=tag_name)
            tag_posts = tag.posts.all()

            return render(request, "blog/tag.html", {
                "tag_name": tag.caption,
                "tag_posts": tag_posts
            })
        except:
            return Http404()


class AuthorPosts(View):
    def get(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            author_posts = author.posts.all()

            return render(request, "blog/author_posts.html", {
                "author_name": f"{author.first_name} {author.last_name}",
                "author_posts": author_posts
            })

        except:
            return Http404()


class AddPost(View):
    def get(self, request):
        try:
            form = AddPostForm()
            return render(request, "blog/add_post.html", {
                "form": form
            })
        except:
            return HttpResponseServerError("Something Went Wrong!!")

    def post(self, request):
        try:
            form = AddPostForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("index"))

            return render(request, "blog/add_post.html", {
                "form": form
            })
        except:
            return HttpResponseServerError("Something Went Wrong!!")

class AddComment(View):
  def get(self,request,id):
    try:
      form = AddCommentForm()
      
      return render(request,"blog/comment_form.html",{
        "form":form
      })
    except:
      return HttpResponseServerError()
  
  def post(self,request,id):
    try:
      form = AddCommentForm(request.POST)
      
      if form.is_valid():
        comment = form.save(commit=False)
        post = Post.objects.get(pk = id)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(reverse("single-post",args=(post.slug,id)))
      
      return render(request,"blog/comment_form.html",{
        "form": form
      })
      
    except:
      return HttpResponseServerError()