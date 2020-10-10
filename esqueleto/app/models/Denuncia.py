from app.models.base import *
from app.models.Comunicante import *
from app.models.Direito import *

class Denuncia(BaseModel):
    comunicante =  models.ForeignKey(Comunicante, on_delete=models.PROTECT)
    direito_violado =  models.ManyToManyField(Direito)
    

    class Meta:
        pass
    