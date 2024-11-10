from django.contrib import admin
from .models import Post, Author, Tag
from datetime import datetime

# Register your models here.

def getNow():
  return datetime.now()

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("title",)}

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)