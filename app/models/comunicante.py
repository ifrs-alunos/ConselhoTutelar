from app.models.base import *
from app.models.endereco import *

class Comunicante(BaseModel):
    nome =  models.CharField(max_length=100,blank=True,null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT,blank=True,null=True)
    
    def __str__(self):
        return self.nome
    class Meta:
        pass
    
