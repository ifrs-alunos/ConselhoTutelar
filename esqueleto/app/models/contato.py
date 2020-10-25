from app.models.base import *
from app.models.comunicante import *

class Contato(BaseModel):
    comunicante = models.ForeignKey(Comunicante, on_delete=models.PROTECT)

    tipo = models.CharField(max_length=100)
    forma = models.CharField(max_length=100)
    def __str__(self):
        return '{} {} : {}'.format(self.comunicante,self.tipo,self.forma)

    class Meta:
        pass
    