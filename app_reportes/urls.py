from django.urls import path
from . import views

app_name = 'app_reportes'
urlpatterns = [
    path('panel/', views.panel_reportes, name='panel_reportes'),
    path('exportar/excel/', views.exportar_excel, name='exportar_excel'),
    path('exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('lista/', views.reporte_reservas, name='lista_reportes'),
    path('generar/', views.generar_reporte_filtrado, name='generar_reporte'),
    path('detalle/<int:pk>/', views.detalle_reporte, name='detalle_reporte'),
]
