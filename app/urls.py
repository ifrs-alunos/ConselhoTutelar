from django.urls import path,include
from django.conf.urls.static import static
from esqueleto import settings

from .views import registro_comunicante, secretaria, lista_denuncia, visualizar_denuncia, lista_vitima, adicionar_anotacao, visualizar_vitima,cadastrar_vitima, ocorrencia,vitima_update,lista_ocorrencia, gerar_pdf_ocorrencia,gerar_pdf_denuncia,gerar_pdf_vitima,dados_gerais, logs_geral, dado_update, dado_add, add_direito

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
    path('listar/dados/<str:acao>',dados_gerais,name="dados_gerais"),
    path('atualizar/<str:objeto>/<int:objeto_id>',dado_update,name='dado_update'),
    path('adicionar/<str:objeto>',dado_add,name='dado_add'),
    path('adicionar/direito/<int:denuncia_id>',add_direito, name='add_direito'),
    path('pdf/ocorrencia/<int:ocorrencia_id>',gerar_pdf_ocorrencia,name='gerar_pdf_ocorrencia'),
    path('pdf/denuncia/<int:denuncia_id>',gerar_pdf_denuncia,name='gerar_pdf_denuncia'),
    path('pdf/vitima/<int:vitima_id>',gerar_pdf_vitima,name='gerar_pdf_vitima'),
    path('logs',logs_geral,name='logs_geral')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)