from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import Signup_Form
# Create your views here.


class Signup_View(generic.CreateView):
    form_class = Signup_Form
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login')
