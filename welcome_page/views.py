from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .models import Application,Blog_Post
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from datetime import datetime

from .forms import CreateBlogPost


# Create your views here.
def index(request):
   return render(request, "welcome_page/index.html")

def thanks(request):
   return render(request, "thanks.html")

def blog(request):
   posts = Blog_Post.objects.all().order_by('-post_date') #Retrieves all blog posts
   return render(request, "welcome_page/blog.html", {'posts' : posts})

def register(request):
   if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)
         return redirect('index')
   else:
      form = UserCreationForm()
   return render(request, 'welcome_page/signup.html', {'form': form})

def login_view(request):
   if(request.method == 'POST'):
      form = AuthenticationForm(request, data = request.POST)
      if form.is_valid():
         user = form.get_user()
         login(request, user)
         return redirect('welcome_page:index')
   else:
      form = AuthenticationForm
   return render(request, 'welcome_page/login.html', {'form':form})

def makePost(request):
    if request.method == 'POST':
        form = CreateBlogPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('welcome_page:blog')  # Replace with your desired redirect URL
    else:
        form = CreateBlogPost()
    return render(request, 'welcome_page/makepost.html', {'form': form})


         

