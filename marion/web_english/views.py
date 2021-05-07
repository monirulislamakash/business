from django.shortcuts import render,redirect
from .models import Head_titel,ProfilUpdate,Android_stor,App_Category,AppList,Content_2
from .models import Blog,Subscription,Our_team,Brand_logo,Category,Course,Content_1
from math import ceil
#add Arabic section
from .models import BlogAR,SubscriptionAR,Our_teamAR,Brand_logoAR,Head_titelAR,CourseAR,Content_2AR
from .models import CategoryAR,Android_storAR,App_CategoryAR,AppListAR,Content_1AR

from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserForm,ProForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    blog=Blog.objects.all()
    team=Our_team.objects.all()
    sliderhead=Head_titel.objects.all()
    contant_1=Content_1.objects.all()
    contant_2=Content_2.objects.all()
    sendblog={
        'blog':blog,
        "team":team,
        "sliderhead":sliderhead,
        "contant_1":contant_1,
        "contant_2":contant_2
    }
    if request.method=="POST":
        subscribe=request.POST.get("Subscription_email")
        mile=Subscription(mail=subscribe)
        mile.save()
    return render(request,"index.html",sendblog)
def blog(request):
    blog=Blog.objects.all()
    blogcategory=Category.objects.all()
    sliderhead=Head_titel.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
        "sliderhead":sliderhead
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
    blogcategory=Category.objects.all()
    sliderhead=Head_titel.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
        "sliderhead":sliderhead
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
    appstor=Android_stor.objects.all()
    appcategory=App_Category.objects.all()
    applist=AppList.objects.all()
    sendvar={
        'apppost':appstor,
        'category':appcategory,
        'applist':applist
    }
    return render(request,"android_stor.html",sendvar)
def allblog(request):
    blog=Blog.objects.filter(category=category)
    blogcategory=Category.objects.all()
    blogpost=Blog.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
        'blogpost':blogpost
    }
    return render(request,"allblog.html",sendblog)
def allblogcategory(request,category):
    blog=Blog.objects.filter(category=category)
    blogcategory=Category.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
    }
    return render(request, "allblogcategory.html",sendblog)
def searchapp(request):
    search=request.POST.get("searchapp")
    appstortitel=Android_stor.objects.filter(titel__icontains=search)
    appstorbody=Android_stor.objects.filter(body__icontains=search)
    appstor=appstortitel.union(appstorbody)
    sendvar={
        'apppost':appstor,
    }
    return render(request,"searchapp.html",sendvar)
def android_course(request):
    allcourse=Course.objects.all()
    sliderhead=Head_titel.objects.all()
    contant_1=Content_1.objects.all()
    contant_2=Content_2.objects.all()
    n= len(allcourse)
    nsliders=n//4 + ceil((n/4)+(n//4))
    sendvar={
        'allcourse':allcourse,
        'sliderhead':sliderhead,
        "contant_1":contant_1,
        "contant_2":contant_2,
        'no_of_slides':nsliders,
        'product': allcourse
    }
    return render(request, "android_course.html",sendvar)
#add Arabic section
def index_ar(request):
    blog=BlogAR.objects.all()
    team=Our_teamAR.objects.all()
    sliderhead=Head_titelAR.objects.all()
    contant_1=Content_1AR.objects.all()
    contant_2=Content_2AR.objects.all()
    sendblog={
        'blog':blog,
        "team":team,
        "sliderhead":sliderhead,
        "contant_1":contant_1,
        "contant_2":contant_2
    }
    if request.method=="POST":
        subscribe=request.POST.get("Subscription_email")
        mile=SubscriptionAR(mail=subscribe)
        mile.save()
    return render(request,"arabic/index_ar.html",sendblog)
def blog_ar(request):
    blog=BlogAR.objects.all()
    blogcategory=CategoryAR.objects.all()
    sliderhead=Head_titelAR.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
        "sliderhead":sliderhead
    }
    return render(request,"arabic/blog_ar.html",sendblog)
def details_blog_ar(request,id):
    blog=BlogAR.objects.filter(id=id)
    sendblog={
        'blog':blog
    }
    return render(request,"details_blog_ar.html",sendblog)
def category_ar(request,category):
    blog=BlogAR.objects.filter(category=category)
    blogcategory=CategoryAR.objects.all()
    sliderhead=Head_titelAR.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
        "sliderhead":sliderhead
    }
    return render(request,"arabic/category_ar.html",sendblog)
def singup_ar(request):
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
                return render(request,"index_ar.html",{'error':"User already exists"})  
            except User.DoesNotExist:
                user=User.objects.create_user(username=email,password=cpassw,first_name=f_name,last_name=l_name)
                return render(request,"index_ar.html",{'success':"user created successfully"})    
        else:
            return render(request,"arabic/index_ar.html")
    else: 
        return redirect(index)
def login_ar(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect(index) 
       else:
            return render(request,"arabic/index_ar.html",{'error_login':"Invalide User and Password"})
    else: 
        return redirect(index)
def logout_ar(request):
    auth.logout(request)
    return redirect(index)
def profile_ar(request):
    return render(request,"arabic/profile_ar.html")
def updateprofile_ar(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            ufrom=UserForm(request.POST,instance=request.user)
            pfrom=ProForm(request.POST,request.FILES,instance=request.user.profilupdate)
            if ufrom.is_valid() and pfrom.is_valid():
                ufrom.save()
                pfrom.save()
                return render(request,"arabic/profile_ar.html",{"pro_update":"Profile Update successfully"})
        else:
            ufrom=UserForm(instance=request.user)
            pfrom=ProForm(instance=request.user.profilupdate)
        return render(request,"arabic/updateprofile_ar.html",{"userfrom":ufrom,"pfrom":pfrom})
    else:
        return redirect(login)
def android_stor_ar(request):
    appstor=Android_storAR.objects.all()
    appcategory=App_CategoryAR.objects.all()
    applist=AppListAR.objects.all()
    sendvar={
        'apppost':appstor,
        'category':appcategory,
        'applist':applist
    }
    return render(request,"arabic/android_stor_ar.html",sendvar)
def allblog_ar(request):
    blog=BlogAR.objects.filter(category=category)
    blogcategory=CategoryAR.objects.all()
    blogpost=BlogAR.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
        'blogpost':blogpost
    }
    return render(request,"arabic/allblog_ar.html",sendblog)
def allblogcategory_ar(request,category):
    blog=BlogAR.objects.filter(category=category)
    blogcategory=CategoryAR.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
    }
    return render(request, "arabic/allblogcategory_ar.html",sendblog)
def searchapp_ar(request):
    search=request.POST.get("searchapp")
    appstortitel=Android_storAR.objects.filter(titel__icontains=search)
    appstorbody=Android_storAR.objects.filter(body__icontains=search)
    appstor=appstortitel.union(appstorbody)
    sendvar={
        'apppost':appstor,
    }
    return render(request,"arabic/searchapp_ar.html",sendvar)
def android_course_ar(request):
    allcourse=CourseAR.objects.all()
    sliderhead=Head_titelAR.objects.all()
    contant_1=Content_1AR.objects.all()
    contant_2=Content_2AR.objects.all()
    n= len(allcourse)
    nsliders=n//4 + ceil((n/4)+(n//4))
    sendvar={
        'allcourse':allcourse,
        'sliderhead':sliderhead,
        "contant_1":contant_1,
        "contant_2":contant_2,
        'no_of_slides':nsliders,
        'product': allcourse
    }
    return render(request, "arabic/android_course_ar.html",sendvar)