# Generated by Django 3.1.1 on 2020-10-10 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Arquivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='')),
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
                ('telefone', models.CharField(max_length=11)),
                ('horario', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Conselheiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('forma', models.CharField(max_length=100)),
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
            name='Direito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_direito', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolha', models.CharField(choices=[('rg', 'RG'), ('cpf', 'CPF')], default='', max_length=3)),
                ('valor', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacao', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('rua', models.CharField(max_length=100)),
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
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anotacoes', models.ManyToManyField(to='app.Anotacao')),
                ('conselheiro', models.ManyToManyField(to='app.Conselheiro')),
                ('denuncia', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.denuncia')),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vitima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('nome_responsavel', models.CharField(max_length=100)),
                ('estudante', models.BooleanField()),
                ('serie', models.IntegerField(choices=[(1, '1° série'), (2, '2° série'), (3, '3° série'), (4, '4° série'), (5, '5° série'), (6, '6° série'), (7, '7° série'), (8, '8° série'), (9, '9° série'), (10, '1° ano'), (11, '2° ano'), (12, '3° ano')], default=' ')),
                ('enderecos', models.ManyToManyField(to='app.Endereco')),
                ('escola', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.escola')),
                ('ocorrencias', models.ManyToManyField(to='app.Ocorrencia')),
            ],
        ),
        migrations.AddField(
            model_name='denuncia',
            name='direito_violado',
            field=models.ManyToManyField(to='app.Direito'),
        ),
        migrations.AddField(
            model_name='comunicante',
            name='documento',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.documento'),
        ),
        migrations.AddField(
            model_name='comunicante',
            name='endereco',
            field=models.ManyToManyField(to='app.Endereco'),
        ),
        migrations.AddField(
            model_name='comunicante',
            name='meio_de_contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.contato'),
        ),
        migrations.AddField(
            model_name='anotacao',
            name='arquivos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.arquivo'),
        ),
    ]
