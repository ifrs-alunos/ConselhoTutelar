from app.models.base import *

class Bairro(BaseModel):
    nome_bairro = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_bairro
    class Meta:
        pass
    