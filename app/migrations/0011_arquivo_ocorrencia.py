# Generated by Django 3.1.2 on 2021-01-18 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210118_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='ocorrencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.ocorrencia'),
        ),
    ]
