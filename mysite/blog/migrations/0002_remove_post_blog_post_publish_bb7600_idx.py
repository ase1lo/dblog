# Generated by Django 4.2.6 on 2023-10-13 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='post',
            name='blog_post_publish_bb7600_idx',
        ),
    ]
