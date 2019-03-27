# Generated by Django 2.1.7 on 2019-03-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='image',
        ),
        migrations.AddField(
            model_name='job',
            name='github_url',
            field=models.CharField(default='https://github.com/SzymonLudyga/', max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='image_url',
            field=models.CharField(default='https://s3.eu-west-2.amazonaws.com/django-static-files-1234/images/', max_length=400),
        ),
    ]
