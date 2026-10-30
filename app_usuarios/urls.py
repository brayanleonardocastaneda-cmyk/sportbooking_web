from django.urls import path
from . import views

app_name = 'app_usuarios'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('perfil/', views.editar_perfil, name='perfil'),
    path('lista/', views.lista_usuarios, name='lista_usuarios'),
    path('panel/', views.panel_admin_view, name='panel_admin'),
]
