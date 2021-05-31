from app.models.base import *
from enum import *
from app.models.comunicante import *

class Tipo(Enum):
    RG = 'rg'
    CPF = 'cpf'
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Documento(BaseModel):
    escolha = models.CharField(choices=Tipo.choices(), max_length=3,blank=True,null=True)
    valor = models.CharField(max_length=11,blank=True,null=True)
    comunicante = models.ForeignKey(Comunicante, on_delete=models.PROTECT,blank=True,null=True)
    def __str__(self):
        return '{} : {}'.format(self.escolha,self.valor)
    class Meta:
        pass