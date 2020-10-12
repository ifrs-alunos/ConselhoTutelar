from app.models.base import *
from app.models.denuncia import *
from app.models.anotacao import *
from app.models.conselheiro import *

class Ocorrencia(BaseModel):
    conselheiro = models.ManyToManyField(Conselheiro)
    denuncia = models.OneToOneField(Denuncia, on_delete=models.PROTECT)
    anotacoes = models.ManyToManyField(Anotacao)

    class Meta:
        pass
    