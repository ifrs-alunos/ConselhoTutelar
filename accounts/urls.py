from django.urls import path,include
from django.conf.urls.static import static
from esqueleto import settings

app_name = 'accounts'

from django.contrib.auth import views as auth_views
from .views import registro, update

urlpatterns = [
    # path('log',login_user,name='login_user'),
    path('log',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login_user'),
    path('registro',registro, name='registro_user'),
    path('logout',auth_views.LogoutView.as_view(next_page='/accounts/log'), name='logout_view'),
    path('update',update, name='update'),
]