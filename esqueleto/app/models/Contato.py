from app.models.base import *

class Contato(BaseModel):
    tipo = models.CharField(max_length=100)
    forma = models.CharField(max_length=100)
    def __str__(self):
        return '{} : {}'.format(self.tipo,self.forma)

    class Meta:
        pass
    