# Generated by Django 4.1.1 on 2022-10-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_followers_postlikes_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='UserId',
            field=models.CharField(default='', max_length=20),
        ),
    ]