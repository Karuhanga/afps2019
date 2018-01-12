from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#View for home
def home(request):
    return render(request, "index.html", {})

#View for Register
def register(request):
    return render(request, "register.html", {})

#View for Event Guide
def event_guide(request):
    return render(request, "event_guide.html", {})

#View for Blog
def blog(request):
    return render(request, "blog.html", {})

#View for Article
def article(request):
    return render(request, "article.html", {})