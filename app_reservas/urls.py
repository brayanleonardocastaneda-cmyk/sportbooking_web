from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Mis reservas</title></head>
<body style="font-family:sans-serif;background:#f9fafb;padding:40px;text-align:center;">
  <h1 style="color:#1e3a8a;">Mis reservas</h1>
  <p style="color:#6b7280;">Próximas / Completadas / Canceladas</p>
  <a href="/reservas/crear/" style="color:#16a34a;">Crear nueva reserva →</a>
</body></html>
"""), name='mis_reservas'),

    path('crear/', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Crear reserva</title></head>
<body style="font-family:sans-serif;background:#f9fafb;padding:40px;text-align:center;">
  <h1 style="color:#1e3a8a;">Crear reserva</h1>
  <a href="/reservas/" style="color:#16a34a;">← Volver a mis reservas</a>
</body></html>
"""), name='crear'),
]