from app.models.base import *
from app.models.Arquivo import *

class Anotacao(BaseModel):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    arquivos = models.ForeignKey(Arquivo, on_delete=models.PROTECT)
    descricao = models.TextField()
    def __str__(self):
        return self.titul
    
    class Meta:
        pass
    