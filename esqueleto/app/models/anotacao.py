from app.models.base import *
from app.models.ocorrencia import *

class Anotacao(BaseModel):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
    
    class Meta:
        pass
        
    