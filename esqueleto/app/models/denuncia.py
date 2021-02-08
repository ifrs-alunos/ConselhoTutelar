from app.models.base import *
from app.models.comunicante import *
from app.models.endereco import *
from django.utils import timezone
from app.models.servidor import *


class Denuncia(BaseModel):
    conselheiro = models.ForeignKey(Servidor, on_delete=models.PROTECT,null=True)
    comunicante =  models.ForeignKey(Comunicante, on_delete=models.PROTECT)
    horario = models.DateTimeField(default=timezone.now)
    endereco_denuncia = models.OneToOneField(Endereco, on_delete=models.PROTECT,blank=True,null=True)
    descricao_situacao = models.TextField()
    nomevitimas = models.TextField()
    class Meta:
        pass
    
            