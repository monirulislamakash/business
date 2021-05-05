"""marion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_english import views

urlpatterns = [
    path('', views.index, name="home"),
    path('blog', views.blog, name="blog"),
    path('singup', views.singup, name="singup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('profile',views.profile,name="profile"),
    path('all_blog',views.allblog,name="allblog"),
    path('all_blog/<str:category>/',views.allblogcategory,name="allblogcategory"),
    path('search_app',views.searchapp,name="searchapp"),
    path('android_stor',views.android_stor,name="android_stor"),
    path('android_course',views.android_course,name="android_course"),
    path('updateprofile',views.updateprofile,name="updateprofile" ),
    path('details_blog/<int:id>/', views.details_blog, name="details_blog"),
    path('category/<str:category>/', views.category, name="category"),
    #Arabic sections add
    path('ar', views.index_ar, name="web_arabic_home"),
    path('ar_blog', views.blog_ar, name="web_arabic_blog"),
    path('ar_singup', views.singup_ar, name="web_arabic_singup"),
    path('ar_login', views.login_ar, name="web_arabic_login"),
    path('ar_logout', views.logout_ar, name="web_arabic_logout"),
    path('ar_profile',views.profile_ar,name="web_arabic_profile"),
    path('ar_all_blog',views.allblog_ar,name="web_arabic_allblog"),
    path('ar_all_blog/<str:category>/',views.allblogcategory_ar,name="web_arabic_allblogcategory"),
    path('ar_search_app',views.searchapp_ar,name="web_arabic_searchapp"),
    path('ar_android_stor',views.android_stor_ar,name="web_arabic_android_stor"),
    path('ar_android_course',views.android_course_ar,name="web_arabic_android_course"),
    path('ar_updateprofile',views.updateprofile_ar,name="web_arabic_updateprofile" ),
    path('ar_details_blog/<int:id>/', views.details_blog_ar, name="web_arabic_details_blog"),
    path('ar_category/<str:category>/', views.category_ar, name="web_arabic_category"),
]
