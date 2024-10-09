from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Application,Blog_Post
from django.utils import timezone

from .forms import ApplicationForm


# Create your views here.
def index(request):
    if request.method == "POST": 
      form = ApplicationForm(request.POST)
      if form.is_valid():
         your_name = form.cleaned_data["your_name"]
         your_dob = form.cleaned_data["your_dob"]
         your_email = form.cleaned_data["your_email"]
         application = Application(
            name = your_name,
            dob = your_dob,
            email = your_email,
            app_date = timezone.now()
         )
         application.save()
         return HttpResponseRedirect("thanks/")
    else:
      return render(request, "welcome_page/index.html")


def get_name(request):
   #if this is a POST request we need to process the form data
   if request.method == "POST":
      #create a form instance and populate it with data from the request:
      form = ApplicationForm(request.POST)
      #check whether it's valid:
      if form.is_valid():
         #process the data in form.cleaned_data as required
         #redirect to a new URL:
         return HttpResponseRedirect("/thanks/")
   else:
      form = ApplicationForm()
   return render(request, "welcome_page/info.html", {"form": form})

def thanks(request):
   return render(request, "thanks.html")

def blog(request):
   posts = Blog_Post.objects.all().order_by('-post_date') #Retrieves all blog posts
   return render(request, "welcome_page/blog.html", {'posts' : posts})