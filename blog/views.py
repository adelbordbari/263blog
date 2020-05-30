from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class post_list(ListView):
    model = Post
    template_name = 'home.html'

class post_details(DetailView):
    model = Post
    template_name = 'post_details.html'