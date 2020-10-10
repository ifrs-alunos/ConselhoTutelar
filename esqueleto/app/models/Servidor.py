from app.models.base import *

class Servidor(BaseModel):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=20)
    email = models.EmailField()
    class Meta:
        abstract = True
        

    