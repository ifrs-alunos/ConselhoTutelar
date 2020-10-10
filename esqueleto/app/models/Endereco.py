from app.models.base import *
from app.models.Cidade import *
from app.models.Bairro import *

class Endereco(BaseModel):
    denominacao = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT,default='')
    complemento = models.CharField(max_length=100)
    numero = models.IntegerField()
    rua = models.CharField(max_length=100)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, default='')
    def __str__(self):
        return '{} {} {} {} '.format(self.rua, self.bairro, self.numero, self.complemento)

    class Meta:
        pass
    