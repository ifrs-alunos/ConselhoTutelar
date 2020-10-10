from app.models.base import *

class Arquivo(BaseModel):
    titulo = models.CharField(max_length=100)
    upload = models.FileField()
    class Meta:
        pass
    