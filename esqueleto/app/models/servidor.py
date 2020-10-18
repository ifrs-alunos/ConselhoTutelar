from app.models.base import *
from django.contrib.auth.models import User 
from app.models.base import BaseModel 
 

class Servidor(BaseModel,User):
    cpf = models.CharField(max_length=11)
    class Meta:
        abstract = True
        

    