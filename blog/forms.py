from django import forms
from .models import Post,Comment

class AddPostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = "__all__"
    exclude = ("slug",)
    labels = {
      "meta":"Description",
      "image":"Cover Image",
    }
    error_messages = {
      "title":{
        "required":"Title is required"
      },
      "image":{
        "required":"Image is required"
      },
    } 
    
class AddCommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = "__all__"
    exclude = ("post",)
    labels = {
      "user_name":"Name",
    }