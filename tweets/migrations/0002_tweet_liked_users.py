# Generated by Django 4.2.2 on 2023-06-18 18:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_tweets', to=settings.AUTH_USER_MODEL),
        ),
    ]
