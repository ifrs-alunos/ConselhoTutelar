from app.models.base import *
from app.models.comunicante import *
from app.models.endereco import *
class Denuncia(BaseModel):
    comunicante =  models.ForeignKey(Comunicante, on_delete=models.PROTECT)
    horario = models.DateTimeField(auto_now_add=True)
    endereco_denuncia = models.OneToOneField(Endereco, on_delete=models.PROTECT)
    descricao_situacao = models.TextField()
    nomevitimas = models.TextField()
    class Meta:
        pass
    
            