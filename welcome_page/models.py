from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length = 100 )
    dob = models.DateTimeField("Date of birth")
    email = models.CharField(max_length = 100)
    app_date = models.DateTimeField("Date application was recieved")


    def __str__(self):
        return self.name
    def applied_recently(self):
        return self.app_date >= timezone.now() - datetime.timedelta(days = 1)

class Blog_Post(models.Model):
    author = models.CharField(max_length = 100, verbose_name ="The name of the author goes here")
    post_date = models.DateTimeField(verbose_name ="Date and time at which the post was created", auto_now_add = True)
    content = models.TextField(verbose_name ="This is where you enter the text of the post")
    image  = models.ImageField(blank = True, null = True, verbose_name ="Optional image")
    video  = models.FileField(blank = True, null = True,verbose_name ="Optional video")  
    
    def __str__(self):
        return f"{self.author} - {self.post_date}"
