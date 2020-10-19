from app.models.base import *
from app.models.endereco import *

class Comunicante(BaseModel):
    nome =  models.CharField(max_length=100)
    endereco = models.ManyToManyField(Endereco)
    def __str__(self):
        return self.nome
    class Meta:
        pass
    
