# Generated by Django 3.1.2 on 2020-12-27 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacao',
            name='arquivos',
            field=models.FileField(null=True, upload_to='imagens_anotacao/'),
        ),
    ]
