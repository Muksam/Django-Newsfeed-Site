from .models import *

def data(request):
    content = {
        'categoryData': Category.objects.prefetch_related('news_set').all(),
    }
    return content

def latest_news(request):
    content = {
        'latestnewsData': LNews.objects.all(),
    }
    return content
