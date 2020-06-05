from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class post_list_view(ListView):
    model = Post
    template_name = 'home.html'


class post_details_view(DetailView):
    model = Post
    template_name = 'post_details.html'


class add_post_view(CreateView):
    model = Post
    template_name = "add_post.html"
    fields =  ['title', 'author', 'body'] # '__all__' for all elements
    prepopulated_fields = {'slug': ('title', )}
