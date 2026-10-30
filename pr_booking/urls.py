from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_escenarios import views as escenario_views
from app_reservas import views as reserva_views
from app_reportes import views as reporte_views
from app_tickets import views as ticket_views
from app_usuarios import views as usuario_views

urlpatterns = [
    path('explorar/', escenario_views.explorar_canchas, name='explorar'),
    path('detalle/<int:pk>/', escenario_views.detalle_cancha, name='detalle_cancha'),
    path('reservas/admin/lista/', reserva_views.lista_reservas_admin, name='lista_reservas_admin'),
    path('reservas/detalle/<int:pk>/', reserva_views.detalle_reserva, name='detalle_reserva'),
    path('reservas/crear/<int:cancha_id>/', reserva_views.crear_reserva, name='crear_reserva'),
    path('reservas/cancelar/<int:pk>/', reserva_views.cancelar_reserva, name='cancelar_reserva'),
    path('reservas/mis/', reserva_views.mis_reservas, name='mis_reservas'),
    path('reservas/completar/<int:pk>/', reserva_views.completar_reserva, name='completar_reserva'),
    path('escenarios/crear/', escenario_views.crear_escenario, name='crear_escenario'),
    path('escenarios/editar/<int:pk>/', escenario_views.editar_escenario, name='editar_escenario'),
    path('escenarios/eliminar/<int:pk>/', escenario_views.eliminar_escenario, name='eliminar_escenario'),
    path('reportes/panel/', reporte_views.panel_reportes, name='panel_reportes'),
    path('tickets/validar/', ticket_views.validar_qr_view, name='validar_qr'),
    path('usuarios/panel/', usuario_views.panel_admin_view, name='panel_admin'),
    path('', include('app_escenarios.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('app_usuarios.urls')),
    path('reservas/', include('app_reservas.urls')),
    path('reportes/', include('app_reportes.urls')),
    path('tickets/', include('app_tickets.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
