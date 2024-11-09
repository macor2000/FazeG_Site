from django.urls import path
#from django.contrib.auth import login,logout,authenticate
from . import views
from django.contrib.auth import views as auth_views
app_name = 'welcome_page'
urlpatterns =[
    path("",views.index, name = 'index'),
    path("thanks/",views.thanks, name = 'thanks'),
    path("blog/",views.blog, name = 'blog'),
    path("signup/", views.register, name = "signup"),
    path("login/", views.login_view, name = "login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='welcome_page:index'), name = 'logout'),
    path("makePost/", views.makePost, name = "makePost"),
   
]