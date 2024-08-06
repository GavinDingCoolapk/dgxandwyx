# Generated by Django 5.0.7 on 2024-08-06 09:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_wish_date_alter_wish_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='wish',
            name='name',
            field=models.CharField(default='Visitor', max_length=20),
        ),
        migrations.AlterField(
            model_name='wish',
            name='post',
            field=models.IntegerField(default=0),
        ),
    ]
