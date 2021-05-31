from app.models.base import *
from app.models.cidade import *


class Bairro(BaseModel):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    def __str__(self):
        return self.nome
    class Meta:
        pass
    