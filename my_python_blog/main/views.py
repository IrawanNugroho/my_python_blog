from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse
from .models import Article



def index(request):
    # latest_article_list = Article.objects.all()
    # tmpJson = serializers.serialize("json", latest_article_list)
    # tmpObj = json.loads(tmpJson)
    # return HttpResponse(json.dumps(tmpObj))
    latest_article_list = Article.objects.order_by('updated_by')[:6]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'base.html', context)
