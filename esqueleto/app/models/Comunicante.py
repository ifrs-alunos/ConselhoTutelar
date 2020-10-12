from app.models.base import *
from app.models.documento import *
from app.models.contato import *
from app.models.endereco import *

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
    vv    pass
    
