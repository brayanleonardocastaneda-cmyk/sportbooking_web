from django.urls import path
from . import views

app_name = 'app_escenarios'
urlpatterns = [
    path('', views.listar_escenarios, name='listar_escenarios'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('explorar/', views.explorar_canchas, name='explorar'),
    path('cancha/<int:pk>/', views.detalle_escenario, name='escenario_detalle'),
    path('detalle/<int:pk>/', views.detalle_cancha, name='detalle_cancha'),
    path('horarios/<int:pk>/', views.horarios_disponibles, name='horarios_disponibles'),
    path('panel/canchas/', views.panel_canchas, name='panel_canchas'),
    path('admin/lista/', views.lista_escenarios_admin, name='lista_escenarios_admin'),
    path('admin/crear/', views.crear_escenario, name='cancha_crear'),
    path('crear/', views.crear_escenario, name='crear_escenario'),
    path('admin/editar/<int:pk>/', views.editar_escenario, name='editar_escenario'),
    path('admin/eliminar/<int:pk>/', views.eliminar_escenario, name='eliminar_escenario'),
]
