from app.models.base import *
from app.models.comunicante import *
from app.models.direito import *

class Denuncia(BaseModel):
    comunicante =  models.ForeignKey(Comunicante, on_delete=models.PROTECT)
    direito_violado =  models.ManyToManyField(Direito)
    descricao_situacao = models.TextField()


    class Meta:
        pass
    