from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from main import models

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path("", TemplateView.as_view(template_name ="home.html"), name="home"),
    path("blog/<slug:slug>/", DetailView.as_view(model=models.Article), name="article"),
]