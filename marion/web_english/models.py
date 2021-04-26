from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.
class Blog(models.Model):
    titel=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    image=models.ImageField(upload_to="static/blog_image/")
    post=RichTextField(blank=True,null=True)
    date=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.titel
class Subscription(models.Model):
    mail=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.mail
class Our_team(models.Model):
    image=models.ImageField(upload_to="static/our_team/")
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    education=models.CharField(max_length=100)
    fb=models.CharField(max_length=200)
    lin=models.CharField(max_length=200)
    git=models.CharField(max_length=200)
    tw=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Brand_logo(models.Model):
    image=models.ImageField(upload_to="static/logo/")
class Head_titel(models.Model):
    titel=models.CharField(max_length=50)
    subtitel=models.CharField(max_length=200)
    button_link=models.CharField(max_length=200)
class Category(models.Model):
    category=models.CharField(max_length=50)
    def __str__(self):
        return self.category
class ProfilUpdate(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    image=models.ImageField(upload_to="static/profile/",default="static/propic/pro_avter.png")
    def __str__(self):
        return str(self.user)
class Android_stor(models.Model):
    titel=models.CharField(max_length=50)
    app_category=models.CharField(max_length=50)
    body=models.TextField()
    image=models.ImageField(upload_to="static/profile/",default="static/Android_stor/")