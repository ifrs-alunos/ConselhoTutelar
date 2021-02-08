from django.urls import path,include
from django.conf.urls.static import static
from esqueleto import settings

from .views import registro_comunicante, secretaria, lista_denuncia, visualizar_denuncia, lista_vitima, adicionar_anotacao, visualizar_vitima,cadastrar_vitima, ocorrencia,vitima_update,lista_ocorrencia

app_name = 'app'


urlpatterns = [
    path('',secretaria , name='secretaria'),
    path('adicionar/comunicante',registro_comunicante , name='registro_comunicante'),
    path('listar/denuncia',lista_denuncia, name='lista_denuncia'),
    path('denuncia/<int:denuncia_id>',visualizar_denuncia, name='visualizar_denuncia'),
    path('adicionar/vitima',cadastrar_vitima, name='cadastrar_vitima'),
    path('listar/vitima',lista_vitima, name='lista_vitima'),
    path('vitima/<int:vitima_id>',visualizar_vitima, name='visualizar_vitima'),
    path('adicionar/anotacao/<int:ocorrencia_id>',adicionar_anotacao, name='adicionar_anotacao'),
    path('vitima/update/<int:vitima_id>',vitima_update, name="vitima_update"),
    path('ocorrencia/<int:ocorrencia_id>',ocorrencia,name="ocorrencia"),
    path('listar/ocorrencia',lista_ocorrencia, name='lista_ocorrencia'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)