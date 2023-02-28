# Generated by Django 4.1.2 on 2022-11-21 11:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Src_App', '0003_comment_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likers',
            field=models.ManyToManyField(related_name='Likers', to=settings.AUTH_USER_MODEL),
        ),
    ]
