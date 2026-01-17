"""
URL configuration for students_records project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from students.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about',about,name="about"),
    path('contactus',contact,name="contactus"),
    path('login',login,name="login"),
    path('admin_dashboard',admin_home,name="admin_dashboard"),
    path('add_stu',add_student,name="add_student"),
    path('view_stu',show_stu,name="view_stu"),
    path('edit_stu/<int:id>',edit_stu,name="edit_stu"),
    path('delete_stu/<int:id>',del_stu,name="del_stu"),
    path('search',search_data,name="search"),
    path('search_stu',search_stu,name="search_stu"),
    path('logout',Logout,name="Logout"),
    path('change_pass',change_pass,name="change_pass"),
    path('account',account,name="account"),
    

    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
