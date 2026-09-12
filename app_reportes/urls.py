from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Dashboard</title></head>
<body style="font-family:sans-serif;background:#f9fafb;padding:40px;text-align:center;">
  <h1 style="color:#1e3a8a;">Panel Administrador</h1>
  <p style="color:#6b7280;">12 reservas · $4.1M · 2/3 canchas · 68%</p>
  <a href="/panel/canchas/" style="color:#16a34a;">Canchas</a> |
  <a href="/panel/horarios/" style="color:#16a34a;">Horarios</a> |
  <a href="/panel/reservas/" style="color:#16a34a;">Reservas</a> |
  <a href="/panel/reportes/" style="color:#16a34a;">Reportes</a> |
  <a href="/panel/validar-qr/" style="color:#16a34a;">QR</a>
</body></html>
"""), name='dashboard'),

    path('canchas/',   lambda request: HttpResponse("<h1>Gestión de canchas</h1><a href='/panel/'>← Panel</a>"), name='canchas'),
    path('horarios/',  lambda request: HttpResponse("<h1>Horarios</h1><a href='/panel/'>← Panel</a>"), name='horarios'),
    path('reservas/',  lambda request: HttpResponse("<h1>Reservas (admin)</h1><a href='/panel/'>← Panel</a>"), name='reservas'),
    path('reportes/',  lambda request: HttpResponse("<h1>Reportes</h1><a href='/panel/'>← Panel</a>"), name='reportes'),
    path('validar-qr/',lambda request: HttpResponse("<h1>Validar QR</h1><a href='/panel/'>← Panel</a>"), name='validar_qr'),
]