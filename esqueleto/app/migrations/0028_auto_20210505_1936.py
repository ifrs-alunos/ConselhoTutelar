# Generated by Django 3.1.6 on 2021-05-05 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20210403_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicante',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.endereco'),
        ),
    ]