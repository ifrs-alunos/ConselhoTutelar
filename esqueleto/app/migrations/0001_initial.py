# Generated by Django 3.1.1 on 2020-10-13 00:59

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anotacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_bairro', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comunicante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('nome', models.CharField(max_length=100)),
                ('horario', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Conselheiro',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_situacao', models.TextField()),
                ('comunicante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.comunicante')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_logradouro', models.CharField(choices=[('Rua', 'Rua'), ('Avenida', 'Avenida'), ('Praça', 'Praça'), ('Quadra', 'Quadra'), ('Alameda', 'Alameda'), ('Beco', 'Beco'), ('Vila', 'Vila'), ('Estrada', 'Estrada'), ('Passagem', 'Passagem'), ('Viela', 'Viela'), ('Servidão', 'Servidão')], default=' ', max_length=20)),
                ('complemento', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('logradouro', models.CharField(max_length=200)),
                ('eatual', models.BooleanField()),
                ('bairro', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='app.bairro')),
                ('cidade', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='app.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_escola', models.CharField(max_length=100)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Vitima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('nome_responsavel', models.CharField(max_length=100)),
                ('enderecos', models.ManyToManyField(to='app.Endereco')),
                ('escola', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.escola')),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conselheiro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.conselheiro')),
                ('denuncia', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.denuncia')),
                ('vitima', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.vitima')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolha', models.CharField(choices=[('rg', 'RG'), ('cpf', 'CPF')], default='', max_length=3)),
                ('valor', models.CharField(max_length=11)),
                ('comunicante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.comunicante')),
            ],
        ),
        migrations.CreateModel(
            name='Direito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_direito', models.CharField(max_length=100)),
                ('denuncia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.denuncia')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('forma', models.CharField(max_length=100)),
                ('comunicante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.comunicante')),
            ],
        ),
        migrations.AddField(
            model_name='comunicante',
            name='endereco',
            field=models.ManyToManyField(to='app.Endereco'),
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='')),
                ('anotacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.anotacao')),
            ],
        ),
        migrations.AddField(
            model_name='anotacao',
            name='ocorrencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.ocorrencia'),
        ),
    ]
