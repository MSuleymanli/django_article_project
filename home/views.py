from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
# from django.http import HttpResponse

# Create your views here.

def home_page(request):
    articles=Article.objects.all()
    return render(request,"home_page.html",{'articles':articles})

def about_page(request):
    return render(request,"about_page.html")


def contact_page(request):
    return render(request,"contact_page.html")


def dashboard_page(request):
    articles=Article.objects.all().filter(author=request.user)
    return render(request,"dashboard_page.html",{'articles':articles})

def articles_page(request):
    articles=Article.objects.all()
    return render(request,"articles_page.html",{'articles':articles})

def addarticle_page(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Your article has been successfully added")
        return redirect("dashboard")

    context = {"form": form}
    return render(request, "addarticle_page.html", context)

def article_detail_page(request, id):
    article = Article.objects.filter(id = id).first()
    context={"article": article}
    return render(request, "article_detail_page.html", context)

