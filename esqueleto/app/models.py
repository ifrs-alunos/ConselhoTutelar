from django.db import models

class Servidor(models.Model):
    senha = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
class Conselheiro(Servidor):
    def cadastravitima(Vitima):
        pass
    def edita_vitima():
        pass
    def consulta_vitima(Vitima):
        pass
    def consulta_denuncia(Denuncia):
        pass
    def cadastra_denuncia(Denuncia):
        pass
    def edita_ccorrencia(Ocorrencia):
        pass
    def acessa_mapa(mapa):
        pass
    
class Secretaria(Servidor):
    def cadastra_comunicante(comunicante):
        pass

class Arquivo(models.Model):
    pass

class Bairro(models.Model):
    nome_bairro = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_bairro
class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_cidade
    
class Endereco(models.Model):
    endereco = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT,default='')
    complemento = models.CharField(max_length=100)
    numero = models.IntegerField()
    rua = models.CharField(max_length=100)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, default='')
    def __str__(self):
        return self.endereco
     
class Contato(models.Model):
    tipo = models.CharField(max_length=100)
    forma = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo


class Comunicante(models.Model):
    data =  models.DateField()
    nome =  models.CharField(max_length=100)
    endereco = models.ManyToManyField(Endereco)
    telefone = models.CharField(max_length=100)
    descricao_situacao = models.CharField(max_length=300)
    horario = models.DateField()
    meio_de_contato = models.ForeignKey(Contato, on_delete=models.PROTECT)
    def __str__(self):
        return self.nome


class Anotacao(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    arquivos = models.ForeignKey(Arquivo, on_delete=models.PROTECT)
    def __str__(self):
        return self.titulo
    
class DireitoViolado(models.Model):
    nome_direito = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_direito

class Escola(models.Model):
    nome_escola = models.CharField(max_length=100)
    endereco = models.ManyToManyField(Endereco)
    def __str__(self):
        return self.nome_escola
class Denuncia(models.Model):
    comunicante =  models.ForeignKey(Comunicante, on_delete=models.PROTECT)
    direito_violado =  models.ManyToManyField(DireitoViolado)
    
    
class Ocorrencia(models.Model):
    denuncia = models.OneToOneField(Denuncia, on_delete=models.PROTECT)
    anotacoes = models.ManyToManyField(Anotacao)
    
    

class Vitima(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nome_responsavel = models.CharField(max_length=100)
    estudante = models.BooleanField()
    serie = models.CharField(max_length=100)
    escola = models.OneToOneField(Escola, on_delete=models.PROTECT)
    endereco = models.ManyToManyField(Endereco)
    ocorrencias = models.ManyToManyField(Ocorrencia) 
    def __str__(self):
        return self.nome
    


    





    
    










