"""OnlineBLOG URL Configuration

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
from homeapp import views as homeViews
from accountapp import views as accountViews
from blogapp import views as blogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.homePage),
    path('blog/logout/', homeViews.logout),
    path('<str:account>/', accountViews.accountBlogHome),
    path('blog/register/', homeViews.register),
    path('blog/regAccOnly/', homeViews.regAccOnly),
    path('blog/VerCodelabel/', homeViews.VerCodesend),
    path('blog/login/', homeViews.login),
    path('<str:account>/publish/', accountViews.gotoPublishBlog),
    path('<str:account>/publish/publishBlog/', accountViews.publishBlog),
]
