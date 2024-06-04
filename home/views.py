from django.shortcuts import render, redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request,"home_page.html")

def about_page(request):
    return render(request,"about_page.html")


def contact_page(request):
    return render(request,"contact_page.html")


def dashboard_page(request):
    articles=Article.objects.all().filter(author=request.user)
    return render(request,"dashboard_page.html",{'articles':articles})

@login_required(login_url="account:login")
def articles_page(request):
    articles=Article.objects.all()
    return render(request,"articles_page.html",{'articles':articles})


@login_required(login_url="account:login")
def article_detail_page(request, id):
    article=get_object_or_404(Article, id=id)
    context={"article": article}
    return render(request, "article_detail_page.html", context)

@login_required(login_url="account:login")
def addarticle_page(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Your article has been successfully added")
        return redirect("dashboard")

    context = {"form": form}
    return render(request, "addarticle_page.html", context)

@login_required(login_url="account:login")
def update_page(request,id):
    article=get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Your article has been successfully Updated")
        return redirect("dashboard")

    context = {"form": form}
    return render(request, "update_page.html", context)


def delete_page(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Your article has been successfully Deleted...")
    return redirect("dashboard")

