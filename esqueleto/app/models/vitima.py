from app.models.base import *
from app.models.escola import *
from app.models.endereco import *
from app.models.choices import SERIE_CHOICES

class Vitima(BaseModel):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True,null=True)
    nome_responsavel = models.CharField(max_length=100,blank=True,null=True)
    escola = models.ForeignKey(Escola, on_delete=models.PROTECT,blank=True,null=True)
    enderecos = models.ManyToManyField(Endereco,blank=True)
    def __str__(self):
        return self.nome

    class Meta:
        pass
    # todo: adicionar script para verificar a maioridade