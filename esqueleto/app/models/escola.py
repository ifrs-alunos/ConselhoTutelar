from app.models.base import *
from app.models.endereco import *

class Escola(BaseModel):
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT,null=True)
    def __str__(self):
        return self.nome
    class Meta:
        pass