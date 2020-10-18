from app.models.base import *
from app.models.anotacao import *

class Arquivo(BaseModel):
    anotacao = models.ForeignKey(Anotacao, on_delete=models.PROTECT)

    titulo = models.CharField(max_length=100)
    upload = models.FileField()
    class Meta:
        pass
    