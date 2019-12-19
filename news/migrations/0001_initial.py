# Generated by Django 2.2.4 on 2019-10-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
    ]
