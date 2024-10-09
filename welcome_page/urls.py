from django.urls import path
from . import views

urlpatterns =[
    path("",views.index, name = 'index'),
    path("info/",views.get_name, name = 'name'),
    path("thanks/",views.thanks, name = 'thanks'),
    path("blog/",views.blog, name = 'blog'),
]