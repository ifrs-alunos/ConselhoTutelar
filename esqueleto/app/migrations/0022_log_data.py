# Generated by Django 3.1.6 on 2021-03-21 00:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='data',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
