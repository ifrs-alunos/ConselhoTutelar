from app.models.base import *
from app.models.cidade import *
from app.models.bairro import *
from app.models.choices import LOGRADOURO_CHOICES
from django.core.exceptions import ValidationError

class Endereco(BaseModel):
    tipo_de_logradouro = models.CharField(choices=LOGRADOURO_CHOICES,max_length=20,blank=True,null=True)
    logradouro = models.CharField(max_length=200,blank=True,null=True)
    numero = models.IntegerField(blank=True,null=True)
    complemento = models.CharField(max_length=100,blank=True,null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT,blank=True,null=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT,blank=True,null=True)
    
    def clean(self):
        # TODO: implementar com classe validator
        if self.bairro:
            if self.bairro not in self.cidade.bairro_set.all():
                raise ValidationError('Bairro não pertence a essa cidade')
            
    def __str__(self):
        return '{} {} {} {} {} '.format(self.tipo_de_logradouro,self.logradouro, self.bairro, self.numero, self.complemento)

    class Meta:
        pass
