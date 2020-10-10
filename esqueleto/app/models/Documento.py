from app.models.base import *


class Documento(BaseModel):
    DOCUMENTO_CHOICES = (
	('rg', 'RG'),
	('cpf', 'CPF'),
    )
    escolha = models.CharField(choices=DOCUMENTO_CHOICES, max_length=3, default='')
    valor = models.CharField(max_length=11)

    def __str__(self):
        return '{} : {}'.format(self.escolha,self.valor)
    class Meta:
        pass