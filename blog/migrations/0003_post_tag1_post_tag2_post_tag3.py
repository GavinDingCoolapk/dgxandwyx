# Generated by Django 5.0.7 on 2024-08-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_style_alter_post_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag1',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='post',
            name='tag2',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='post',
            name='tag3',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
