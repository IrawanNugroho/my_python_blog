from django.shortcuts import render
from .models import Article



def index(request):
    latest_article_list = Article.objects.order_by('-updated_by')[:6]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'base.html', context)
