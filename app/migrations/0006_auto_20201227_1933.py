# Generated by Django 3.1.2 on 2020-12-27 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201227_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anotacao',
            name='arquivos',
        ),
        migrations.DeleteModel(
            name='AnotacaoFile',
        ),
    ]
