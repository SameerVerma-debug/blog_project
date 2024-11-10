from django.http import Http404, HttpResponse, HttpResponseServerError
from django.shortcuts import render
from .models import Post, Tag, Author
import heapq

LATEST_POSTS_NUM = 3

# Create your views here.

# get three latest posts and send back some welcome text along with 3 latest posts


def index(request):
    try:
        latest_posts = []
        pq = []
        heapq.heapify(pq)
        
        all_posts = Post.objects.all()
        
        for post in all_posts:
          if len(pq) < LATEST_POSTS_NUM:
            heapq.heappush(pq,(post.date,post))
          else:
            if pq[0][0] < post.date:
              heapq.heappop(pq)
              heapq.heappush(pq,(post.date,post))

        for _,post in pq:
          latest_posts.append(post)
        
        return render(request,"blog/index.html",{
          "posts":latest_posts
        })
    except:
        return HttpResponseServerError("Something Went Wrong!!")


def posts(request):
    try:
      all_posts = Post.objects.all() 
      return render(request,"blog/posts.html",{
        "posts":all_posts
      })
    except:
      return HttpResponseServerError("Something Went Wrong!!")


def single_post(request, slug, id):
  try:
    found_post = Post.objects.get(slug = slug.lower(), id = int(id))
    found_post_tags = found_post.tags.all()
    
    return render(request,"blog/post.html",{
      "post":found_post,
      "post_tags":found_post_tags
    })
  except:
    raise Http404()
  

def tag_posts(request, tag_name):
  try:
    tag = Tag.objects.get(caption=tag_name)
    tag_posts = tag.posts.all()
    
    return render(request,"blog/tag.html",{
      "tag_name": tag.caption,
      "tag_posts": tag_posts
    })
  except:
    return Http404()
    
def author_posts(request, id):
  try:
    author = Author.objects.get(pk=id)
    author_posts = author.posts.all()
    
    return render(request,"blog/author_posts.html",{
      "author_name": f"{author.first_name} {author.last_name}",
      "author_posts": author_posts
    })
    
  except:
    return Http404()