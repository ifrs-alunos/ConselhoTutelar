from app.models.base import *
from app.models.denuncia import *
from app.models.anotacao import *
from app.models.conselheiro import *
from app.models.vitima import *

class Ocorrencia(BaseModel):
    conselheiro = models.ForeignKey(Conselheiro, on_delete=models.PROTECT)
    denuncia = models.OneToOneField(Denuncia, on_delete=models.PROTECT)
    vitima = models.ForeignKey(Vitima, on_delete=models.PROTECT)

    
    class Meta:
        pass