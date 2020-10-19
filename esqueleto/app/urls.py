from django.urls import path

from .views import registro_comunicante, secretaria

urlpatterns = [
    path('',secretaria , name='secretaria'),
     path('registro_comunicante',registro_comunicante , name='registro_comunicante')
]