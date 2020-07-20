from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import *


class post_list_view(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_on']


class post_details_view(DetailView):
    model = Post
    template_name = 'post_details.html'


class add_post_view(CreateView):
    model = Post
    template_name = "add_post.html"
    # if a form is being used, it needs to be mentioned. the line below is added later
    # also when using forms, we need to omit "fields", hence the comment
    form_class = PostForm
    # fields = ['author', 'title', 'body']  # '__all__' for all elements


class update_post_view(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm


class delete_post_view(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
