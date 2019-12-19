from .models import *

def data(request):
    content = {
        'categoryData': Category.objects.prefetch_related('news_set').all(),
    }
    return content


def slid(request):
    content = {
        'sliderData': Slider.objects.prefetch_related('slider_set').all()
    }
    return content