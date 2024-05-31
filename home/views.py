from django.shortcuts import render
from .models import Article
# from django.http import HttpResponse

# Create your views here.

def home_page(request):
    articles=Article.objects.all()
    return render(request,"home_page.html",{'articles':articles})

def about_page(request):
    return render(request,"about_page.html")


def contact_page(request):
    return render(request,"contact_page.html")