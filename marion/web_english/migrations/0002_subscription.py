# Generated by Django 3.2 on 2021-04-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_english', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=50)),
            ],
        ),
    ]
