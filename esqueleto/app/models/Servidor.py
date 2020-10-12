from app.models.base import *
from django.contrib.auth.models import User 
from app.models.base import BaseModel 
 

class Servidor(BaseModel,User):
    pass
    class Meta:
        abstract = True
        

    