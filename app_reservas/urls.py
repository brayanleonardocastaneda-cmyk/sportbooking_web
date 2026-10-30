from django.urls import path
from . import views

app_name = 'app_reservas'
urlpatterns = [
    path('panel/', views.panel_reservas, name='panel_reservas'),
    path('admin/lista/', views.lista_reservas_admin, name='lista_reservas_admin'),
    path('reservar/<int:cancha_id>/', views.reservar, name='reservar'),
    path('crear/<int:cancha_id>/', views.crear_reserva, name='crear_reserva'),
    path('confirmada/<int:pk>/', views.reserva_confirmada, name='reserva_confirmada'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('cancelar/<int:pk>/', views.reserva_cancelar, name='reserva_cancelar'),
    path('detalle/<int:pk>/', views.detalle_reserva, name='detalle_reserva'),
    path('completar/<int:pk>/', views.completar_reserva, name='completar_reserva'),
    path('exportar/', views.reservas_exportar, name='reservas_exportar'),
]
