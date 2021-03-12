# Generated by Django 2.2.4 on 2020-01-13 11:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20191101_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='LNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='news')),
                ('description', ckeditor.fields.RichTextField()),
                ('status', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Latest News',
            },
        ),
    ]
