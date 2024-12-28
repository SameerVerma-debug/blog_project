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
    
class AddCommentForm(forms.Form):
  name = forms.CharField(max_length=50,label="Name",error_messages={
    "required": "Name is required"
  })
  description = forms.CharField(widget=forms.Textarea())