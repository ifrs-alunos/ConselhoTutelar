from app.models.base import *
from app.models.denuncia import *
from app.models.anotacao import *
from app.models.servidor import *
from app.models.vitima import *

class Ocorrencia(BaseModel):
    denuncia = models.OneToOneField(Denuncia, on_delete=models.PROTECT)
    vitimas = models.ManyToManyField(Vitima)
    
    class Meta:
        pass