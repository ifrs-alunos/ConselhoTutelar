from django.db import models
from .log import Log


class BaseModel(models.Model):

    def save(self, *args, **kwargs): 
        try:
            if self.pk :
                orig = self.__class__.objects.get(id=self.id)
                fields = [field for field in self._meta.fields]
                for field in fields:
                    name = field.name
                    if getattr(orig,  name) != getattr(self,  name):
                        if getattr(orig,  name):
                            log = Log(model=self.__class__.__name__, atributo_mudado=name,antes=getattr(orig,  name),agora=getattr(self,  name))
                            log.save()
            else:
                fields = [field for field in self._meta.fields]
                for field in fields:
                    name = field.name
                    if name != 'id':
                        log = Log(model=self.__class__.__name__, atributo_mudado=name,antes='',agora=getattr(self,  name))
                        log.save()
        except:
            pass
        super(BaseModel, self).save(*args, **kwargs) 

    class Meta:
        abstract = True
        app_label = 'blank'
        