from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('escenarios/', include('app_escenarios.urls')),
    path('reservas/',   include('app_reservas.urls')),
    path('usuarios/',   include('app_usuarios.urls')),
    path('reportes/',      include('app_reportes.urls')),
]