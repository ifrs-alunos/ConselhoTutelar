from app.models.base import *
from app.models.cidade import *


class Bairro(BaseModel):
    nome_bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome_bairro
    class Meta:
        pass
    