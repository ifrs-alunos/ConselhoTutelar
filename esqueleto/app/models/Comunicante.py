from app.models.base import *
from app.models.Documento import *
from app.models.Contato import *
from app.models.Endereco import *

class Comunicante(BaseModel):
    data =  models.DateField()
    nome =  models.CharField(max_length=100)
    endereco = models.ManyToManyField(Endereco)
    telefone = models.CharField(max_length=11)
    horario = models.DateField()
    meio_de_contato = models.ForeignKey(Contato, on_delete=models.PROTECT)
    documento = models.OneToOneField(Documento, on_delete=models.PROTECT)
    def __str__(self):
        return self.nome
    class Meta:
        pass
    
