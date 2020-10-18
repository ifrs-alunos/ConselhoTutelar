from app.models.base import *
from app.models.endereco import *

class Comunicante(BaseModel):
    data =  models.DateField()
    nome =  models.CharField(max_length=100)
    endereco = models.ManyToManyField(Endereco)
    horario = models.DateField()
    def __str__(self):
        return self.nome
    class Meta:
        pass
    
