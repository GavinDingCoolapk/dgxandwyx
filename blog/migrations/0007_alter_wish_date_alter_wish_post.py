# Generated by Django 5.0.7 on 2024-08-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_wish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='wish',
            name='post',
            field=models.IntegerField(),
        ),
    ]
