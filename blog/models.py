from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email_address = models.EmailField()
  
  def __str__(self):
    return f"{self.first_name} {self.last_name} ({self.email_address})"
  
  def get_absolute_url(self):
      return reverse("author-posts", args=[self.pk])
  

class Tag(models.Model):
  caption = models.CharField(max_length=100)
  
  def __str__(self):
    return f"{self.caption}"
  
  def get_absolute_url(self):
      return reverse("tag-posts", args=[self.caption])  

class Post(models.Model):
  title=models.CharField(max_length=200)
  meta = models.TextField()
  image = models.ImageField(upload_to="images",null=True)
  date = models.DateTimeField(auto_now=True)
  slug = models.SlugField(db_index=True)
  content = models.TextField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
  tags = models.ManyToManyField(Tag,related_name="posts")
  
  def __str__(self):
    return f"{self.title} by {self.author.first_name} {self.author.last_name}"
  
  def save(self,*args, **kwargs):
    self.slug = slugify(self.title)
    self.date = datetime.now()
    super().save(*args,**kwargs)
    
  def get_absolute_url(self):
      return reverse("single-post",args=[self.slug,self.id])
  
  
class Comment(models.Model):
  user_name = models.CharField(max_length=50)
  description = models.TextField()
  date = models.DateField(auto_now=True)
  post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
  
  def __str__(self):
    return f"By {self.user_name} on post {self.post.title}"
  