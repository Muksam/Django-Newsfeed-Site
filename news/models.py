from django.db import models
from django.utils import timezone
from django.contrib.auth.admin import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    cat_name = models.CharField(max_length= 100, unique=True)
    status = models.BooleanField(default=0)


    def __str__(self):
        return self.cat_name

    class Meta:
         verbose_name_plural = 'Category'



class News(models.Model):
    posted_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='news')
    description = RichTextField()
    status = models.BooleanField(default=0)


    class Meta:
         verbose_name_plural = 'News'


class Slider(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(blank=True, upload_to='news')
    description = RichTextField()
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.title


    class Meta:
         verbose_name_plural = 'Slider'


