from app.models.base import *
from enum import Enum

class Tipo(Enum):
    RG = 'rg'
    CPF = 'cpf'

class Documento(BaseModel):
    escolha = models.CharField(choices=Tipo, max_length=3, default='')
    valor = models.CharField(max_length=11)

    def __str__(self):
        return '{} : {}'.format(self.escolha,self.valor)
    class Meta:
        pass