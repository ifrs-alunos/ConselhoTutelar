# Generated by Django 3.1.2 on 2021-01-04 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201227_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='endereco_denuncia',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.endereco'),
        ),
    ]
