from django.shortcuts import render
from .models import Article
from .models import Blog

# Create your views here.
def home(request):
    article = Article.objects
    return render(request,'home.html', {'article':article})

def home(request):
    blog = Article.objects
    return render(request,'home.html',)
