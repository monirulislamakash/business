from django.contrib import admin
from .models import Blog,Subscription,Our_team,Brand_logo,Head_titel,Course
from .models import Category,ProfilUpdate,Android_stor,App_Category,AppList,Content_1,Content_2
#add arabic section
from .models import BlogAR,SubscriptionAR,Our_teamAR,Brand_logoAR,Head_titelAR,CourseAR
from .models import CategoryAR,Android_storAR,App_CategoryAR,AppListAR,Content_1AR,Content_2AR
# Register your models here.
admin.site.register(Blog)
admin.site.register(Subscription)
admin.site.register(Our_team)
admin.site.register(Brand_logo)
admin.site.register(Head_titel)
admin.site.register(Category)
admin.site.register(ProfilUpdate)
admin.site.register(Android_stor)
admin.site.register(App_Category)
admin.site.register(AppList)
admin.site.register(Course)
admin.site.register(Content_1)
admin.site.register(Content_2)
#add arabic section
admin.site.register(BlogAR)
admin.site.register(SubscriptionAR)
admin.site.register(Our_teamAR)
admin.site.register(Brand_logoAR)
admin.site.register(Head_titelAR)
admin.site.register(CategoryAR)
admin.site.register(Android_storAR)
admin.site.register(App_CategoryAR)
admin.site.register(AppListAR)
admin.site.register(CourseAR)
admin.site.register(Content_1AR)
admin.site.register(Content_2AR)