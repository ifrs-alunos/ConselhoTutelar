from app.models.base import *

class Direito(BaseModel):
    nome_direito = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_direito

    class Meta:
        pass
    