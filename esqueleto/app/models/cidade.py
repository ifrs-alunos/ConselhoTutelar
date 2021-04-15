from app.models.base import *


class Cidade(BaseModel):
    nome= models.CharField(max_length=100)

    @classmethod
    def dicionario_cidade_bairro(cls):
        dicionario_cidade = {}
        cidades = cls.objects.all()
        lista_bairro = []
        
        for cidade in cidades:
            bairros = cidade.bairro_set.all()
            for bairro in bairros:
                bairro = bairro.id
                lista_bairro.append(bairro)
            dicionario_cidade[cidade.id] = lista_bairro
            lista_bairro =[]
        return dicionario_cidade
  
    def __str__(self):
        return self.nome
    class Meta:
        pass

   