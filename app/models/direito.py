from app.models.base import *
from app.models.denuncia import *

class Direito(BaseModel):
    denuncia = models.ForeignKey(Denuncia, on_delete=models.PROTECT,null=True)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

    class Meta:
        pass
    