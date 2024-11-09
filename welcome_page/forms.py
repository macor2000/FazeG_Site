from django import forms
from .models import Blog_Post
#Defining a form class with three fields.


class CreateBlogPost(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = '__all__'