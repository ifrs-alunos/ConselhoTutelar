# Generated by Django 3.1.6 on 2021-04-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20210321_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='agora',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]