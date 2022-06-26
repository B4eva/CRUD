from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post


# Create your views here.








class PostListView(CreateView):
    model: Post

class  PostCreateView(CreateView): 
    model = Post
    fields = [
        'title',
         'body'
      ]
class PostDetailView(CreateView):
    model: Post


class PostUpdateView(CreateView):
    model: Post
    fields = [ 
        'title',
         'body'
    ]

class PostDeleteView(CreateView):
    model: Post
    fields = [
              'title',
         'body'
    ]



    template_name: 'base.html'
    


