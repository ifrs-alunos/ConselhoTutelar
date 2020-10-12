from app.models.base import *
from app.models.comunicante import *

class Denuncia(BaseModel):
    comunicante =  models.ForeignKey(Comunicante, on_delete=models.PROTECT)
    descricao_situacao = models.TextField()


    class Meta:
        pass
    