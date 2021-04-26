from django.shortcuts import render,redirect
from .models import Blog,Subscription,Our_team,Brand_logo,Category,Head_titel,ProfilUpdate
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserForm,ProForm
# Create your views here.
def index(request):
    blog=Blog.objects.all()
    team=Our_team.objects.all()
    sendblog={
        'blog':blog,
        "team":team
    }
    if request.method=="POST":
        subscribe=request.POST.get("Subscription_email")
        mile=Subscription(mail=subscribe)
        mile.save()
    return render(request,"index.html",sendblog)
def blog(request):
    blog=Blog.objects.all()
    blogcategory=Category.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory
    }
    return render(request,"blog.html",sendblog)
def details_blog(request,id):
    blog=Blog.objects.filter(id=id)
    sendblog={
        'blog':blog
    }
    return render(request,"details_blog.html",sendblog)
def category(request,category):
    blog=Blog.objects.filter(category=category)
    sendblog={
        'blog':blog
    }
    return render(request,"category.html",sendblog)
def singup(request):
    f_name=request.POST.get("f_name")
    l_name=request.POST.get("l_name")
    email=request.POST.get("email")
    passw=request.POST.get("password")
    cpassw=request.POST.get("confirmpassword")
    propic=request.FILES["propic"] 
    if request.method=="POST":
        if passw==passw:
            try:
                user=User.objects.get(username=email)
                return render(request,"index.html",{'error':"User already exists"})  
            except User.DoesNotExist:
                user=User.objects.create_user(username=email,password=cpassw,first_name=f_name,last_name=l_name)
                return render(request,"index.html",{'success':"user created successfully"})    
        else:
            return render(request,"index.html")
    else: 
        return redirect(index)
def login(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect(index) 
       else:
            return render(request,"index.html",{'error_login':"Invalide User and Password"})
    else: 
        return redirect(index)
def logout(request):
    auth.logout(request)
    return redirect(index)
def profile(request):
    return render(request,"profile.html")
def updateprofile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            ufrom=UserForm(request.POST,instance=request.user)
            pfrom=ProForm(request.POST,request.FILES,instance=request.user.profilupdate)
            if ufrom.is_valid() and pfrom.is_valid():
                ufrom.save()
                pfrom.save()
                return render(request,"profile.html",{"pro_update":"Profile Update successfully"})
        else:
            ufrom=UserForm(instance=request.user)
            pfrom=ProForm(instance=request.user.profilupdate)
        return render(request,"updateprofile.html",{"userfrom":ufrom,"pfrom":pfrom})
    else:
        return redirect(login)
def android_stor(request):
     return render(request,"android_stor.html")