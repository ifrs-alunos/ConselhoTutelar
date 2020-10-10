from app.models.base import *

class Cidade(BaseModel):
    nome_cidade = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_cidade

    class Meta:
        pass
    