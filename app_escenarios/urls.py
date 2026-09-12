from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Inicio</title></head>
<body style="font-family:sans-serif;background:#f9fafb;padding:40px;text-align:center;">
  <h1 style="color:#1e3a8a;">Inicio - Canchas</h1>
  <p style="color:#6b7280;">Canchas destacadas.</p>
  <a href="/escenarios/buscar/" style="color:#16a34a;">Buscar</a> |
  <a href="/escenarios/favoritos/" style="color:#16a34a;">Favoritos</a> |
  <a href="/reservas/" style="color:#16a34a;">Mis reservas</a>
</body></html>
"""), name='home'),

    path('buscar/', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Buscar</title></head>
<body style="font-family:sans-serif;background:#f9fafb;padding:40px;text-align:center;">
  <h1 style="color:#1e3a8a;">Buscar canchas</h1>
  <a href="/escenarios/1/" style="color:#16a34a;">Ver detalle cancha #1 →</a>
</body></html>
"""), name='buscar'),

    path('<int:pk>/', lambda request, pk: HttpResponse(f"""
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Detalle</title></head>
<body style="font-family:sans-serif;background:#f9fafb;padding:40px;text-align:center;">
  <h1 style="color:#1e3a8a;">Detalle cancha #{pk}</h1>
  <a href="/reservas/crear/" style="color:#16a34a;">Reservar ahora →</a>
</body></html>
"""), name='detalle'),

    path('favoritos/', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Favoritos</title></head>
<body style="font-family:sans-serif;background:#f9fafb;padding:40px;text-align:center;">
  <h1 style="color:#1e3a8a;">Mis favoritos</h1>
</body></html>
"""), name='favoritos'),
]