"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from home.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home_page, name="home"),
    path("contact",contact_page, name="contact"),
    path("account/",include("account.urls")),
    path("dashboard",dashboard_page,name="dashboard"),
    path("articles",articles_page,name="articles"),
    path("article_detail/<int:id>",article_detail_page,name="article_detail"),
    path("addarticle",addarticle_page,name="addarticle"),
    path("update/<int:id>",update_page,name="update"),
    path("delete/<int:id>",delete_page,name="delete"),
    path("comment/<int:id>",addcomment_page,name="comment")

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
