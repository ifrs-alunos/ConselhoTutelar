from app.models.base import *
from app.models.escola import *
from app.models.endereco import *
from app.models.ocorrencia import *
from app.models.choices import SERIE_CHOICES

class Vitima(BaseModel):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nome_responsavel = models.CharField(max_length=100)
    estudante = models.BooleanField()
    escola = models.OneToOneField(Escola, on_delete=models.PROTECT)
    enderecos = models.ManyToManyField(Endereco)
    ocorrencias = models.ManyToManyField(Ocorrencia) 
    
    serie = models.IntegerField(choices=SERIE_CHOICES,default=' ')

    
    def __str__(self):
        return self.nome

    class Meta:
        pass
    