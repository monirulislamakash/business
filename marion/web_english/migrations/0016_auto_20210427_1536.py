# Generated by Django 3.2 on 2021-04-27 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_english', '0015_auto_20210427_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='android_stor',
            name='image',
            field=models.ImageField(default='', upload_to='static/android_stor/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 15, 36, 28, 177695)),
        ),
    ]