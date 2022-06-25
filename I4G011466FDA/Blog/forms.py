from dataclasses import field
from pyexpat import model
from django import forms
from .models import Post 

class PostForm(forms): 
     class Meta: 
        model = Post
        fields = [ 
            'title',
            'body'
        ]