from app.models.base import *
from app.models.cidade import *
from app.models.bairro import *
from app.models.choices import LOGRADOURO_CHOICES

class Endereco(BaseModel):
    tipo_de_logradouro = models.CharField(choices=LOGRADOURO_CHOICES,default=' ', max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT,default='')
    complemento = models.CharField(max_length=100)
    numero = models.IntegerField()
    logradouro = models.CharField(max_length=200)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, default='')
    eatual = models.BooleanField()
    # TODO: FAZER UMA VERIFICAÇÃO ANTES DE SALVAR SE UM BAIRRO PERTENCE A UMA CIDADE
    def __str__(self):
        return '{} {} {} {} {} '.format(self.tipo_de_logradouro,self.logradouro, self.bairro, self.numero, self.complemento)

    class Meta:
        pass
