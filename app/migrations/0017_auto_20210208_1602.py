# Generated by Django 3.1.6 on 2021-02-08 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210122_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vitima',
            name='enderecos',
        ),
        migrations.AddField(
            model_name='vitima',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.endereco'),
        ),
    ]