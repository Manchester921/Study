"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app01 import views as app01_v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', app01_v.gotoTest),
    path('add/<int:num1>+<int:num2>', app01_v.gotoAdds),
    path('', app01_v.gotoLogin),
    path('register/', app01_v.gotoRegister),
    path('blog/', app01_v.blogLogin), 
    path('blog/logout/', app01_v.logout), 
    path('category/add/', app01_v.logout), 
    
]
