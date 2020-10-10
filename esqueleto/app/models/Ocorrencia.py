from app.models.base import *
from app.models.Denuncia import *
from app.models.Anotacao import *
from app.models.Conselheiro import *

class Ocorrencia(BaseModel):
    conselheiro = models.ManyToManyField(Conselheiro)
    denuncia = models.OneToOneField(Denuncia, on_delete=models.PROTECT)
    anotacoes = models.ManyToManyField(Anotacao)

    class Meta:
        pass
    