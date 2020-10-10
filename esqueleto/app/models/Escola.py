from app.models.base import *
from app.models.Endereco import *

class Escola(BaseModel):
    nome_escola = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    def __str__(self):
        return self.nome_escola
    class Meta:
        pass