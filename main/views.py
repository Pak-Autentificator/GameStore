from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

#-----------------------------------------------------------------------------------------

def index(request):
    new_post = Post.objects.all()
    return render(request, 'main/index.html', {'new_post': new_post})

def sell(request):
    return render(request, 'main/sell.html')

def test(request):
    return render(request, 'main/test.html')

#-----------------------------------------------------------------------------------------




























