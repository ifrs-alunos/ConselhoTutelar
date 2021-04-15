from django_currentuser.db.models import CurrentUserField
from django.db import models
from django.utils import timezone


class Log(models.Model):
    servidor = CurrentUserField()
    model = models.CharField(max_length=100)
    atributo_mudado = models.CharField(max_length=100)
    antes = models.CharField(max_length=100)
    agora = models.CharField(max_length=100,blank=True,null=True,default='')
    data = models.DateTimeField(default=timezone.now)



    
    def __str__(self):
        return f'Servidor: {self.servidor}, Modelo: {self.model}, Atributo {self.atributo_mudado}: {self.antes} -> {self.agora}, Data: {self.data}'
    class Meta:
        pass