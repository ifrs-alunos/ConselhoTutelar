from app.models.base import *
from app.models.Escola import *
from app.models.Endereco import *
from app.models.Ocorrencia import *

class Vitima(BaseModel):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nome_responsavel = models.CharField(max_length=100)
    estudante = models.BooleanField()
    escola = models.OneToOneField(Escola, on_delete=models.PROTECT)
    enderecos = models.ManyToManyField(Endereco)
    ocorrencias = models.ManyToManyField(Ocorrencia) 
    SERIE_CHOICES = (
	(1, '1° série'),
	(2, '2° série'),
	(3, '3° série'),
	(4, '4° série'),
	(5, '5° série'),
	(6, '6° série'),
	(7, '7° série'),
	(8, '8° série'),
	(9, '9° série'),
	(10, '1° ano'),
	(11, '2° ano'),
	(12, '3° ano')
    )
    serie = models.IntegerField(choices=SERIE_CHOICES,default=' ')

    
    def __str__(self):
        return self.nome

    class Meta:
        pass
    