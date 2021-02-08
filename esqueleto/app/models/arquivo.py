from app.models.base import *
from app.models.anotacao import *

class Arquivo(BaseModel):
    titulo = models.CharField(max_length=100,blank=True,null=True)
    upload = models.FileField(blank=True,null=True)
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.PROTECT,blank=True,null=True)
    anotacao = models.ForeignKey(Anotacao, on_delete=models.PROTECT,blank=True,null=True)


    class Meta:
        pass
    