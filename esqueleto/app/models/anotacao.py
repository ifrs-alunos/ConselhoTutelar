from app.models.base import *
from app.models.ocorrencia import *
from django.utils import timezone

class Anotacao(BaseModel):
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
    
    class Meta:
        pass
        
    