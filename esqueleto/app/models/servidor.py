from app.models.base import *
from django.contrib.auth.models import User 
from app.models.base import BaseModel 
 

class Servidor(BaseModel,User):
    cpf = models.CharField(max_length=11)

    @classmethod
    def conselheiro_para_denuncia(cls):
        lista_val = []
        menos_casos = 0
        sortudo = 0
        conselheiros = cls.objects.filter(groups__name='Conselheiros')
        for conselheiro in conselheiros:
            denuncias = len(conselheiro.denuncia_set.all())
            lista_val.append(denuncias)

        menor = min(lista_val)
        
        for c in conselheiros:
            denuncias = len(c.denuncia_set.all())
            if denuncias == menor:
                sortudo = c
                
        return sortudo.id


    class Meta:
        pass
    