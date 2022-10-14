from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from articles.forms import ArticleForm 

# Create your views here.

def index(request):
    articles = Review.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            article_form = ArticleForm(request.POST)
            if article_form.is_valid():
                article_form.save()
                return redirect('articles:index')
        else:
            article_form = ArticleForm()
        context = {
            'article_form':article_form
        }
        return render(request, 'articles/forms.html', context)
    else:
        return redirect('accounts:login')