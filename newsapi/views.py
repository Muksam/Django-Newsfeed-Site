from django.shortcuts import render

from .serializers import NewsSerializer

from news.models import News
from rest_framework import viewsets


class NewsApiDetails(viewsets.ModelViewSet) :
    queryset = News.objects.all()
    serializer_class = NewsSerializer


