from django.db import models
from django.utils.text import slugify
from datetime import datetime

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email_address = models.EmailField()
  
  def __str__(self):
    return f"{self.first_name} {self.last_name} ({self.email_address})"

class Post(models.Model):
  title=models.CharField(max_length=200)
  meta = models.TextField()
  image_url = models.URLField()
  date = models.DateTimeField()
  slug = models.SlugField(db_index=True)
  content = models.TextField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.title} by {self.author.first_name} {self.author.last_name}"
  
  def save(self,*args, **kwargs):
    self.slug = slugify(self.title)
    self.date = datetime.now()
    super().save(*args,**kwargs)
  
class Tag(models.Model):
  caption = models.CharField(max_length=100)
  posts_list = models.ManyToManyField(Post)
  
  def __str__(self):
    return f"{self.caption}"