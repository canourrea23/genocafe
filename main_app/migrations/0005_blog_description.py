# Generated by Django 3.1.5 on 2021-01-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210126_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default='', max_length=450),
        ),
    ]
