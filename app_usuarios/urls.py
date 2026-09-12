from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Login - SportBooking</title>
<style>
  *{margin:0;padding:0;box-sizing:border-box;font-family:'Inter',system-ui,sans-serif;}
  body{background:#f9fafb;min-height:100vh;}
  .header{background:linear-gradient(135deg,#22c55e 0%,#1e3a8a 100%);padding:60px 24px 80px;
    text-align:center;color:#fff;border-bottom-left-radius:40px;border-bottom-right-radius:40px;}
  .logo{width:72px;height:72px;margin:0 auto 16px;background:rgba(255,255,255,.15);
    border-radius:20px;display:flex;align-items:center;justify-content:center;font-size:36px;}
  .header h1{font-size:28px;margin-bottom:6px;}
  .header p{font-size:15px;opacity:.9;}
  .wrap{max-width:480px;margin:0 auto;padding:32px 24px 40px;}
  .wrap h2{font-size:26px;color:#1e3a8a;margin-bottom:6px;}
  .sub{color:#6b7280;font-size:15px;margin-bottom:28px;}
  .input-group{position:relative;margin-bottom:16px;}
  .input-group input{width:100%;padding:18px 20px 18px 52px;border:1px solid #e5e7eb;
    border-radius:14px;font-size:15px;background:#fff;outline:none;}
  .input-group input:focus{border-color:#22c55e;box-shadow:0 0 0 3px rgba(34,197,94,.1);}
  .icon{position:absolute;left:18px;top:50%;transform:translateY(-50%);color:#9ca3af;font-size:18px;}
  .forgot{display:block;text-align:right;color:#16a34a;font-size:14px;
    text-decoration:none;margin-bottom:24px;font-weight:500;}
  .btn{width:100%;padding:18px;background:linear-gradient(135deg,#22c55e,#16a34a);
    color:#fff;border:none;border-radius:14px;font-size:16px;font-weight:600;cursor:pointer;}
  .divider{display:flex;align-items:center;gap:12px;color:#9ca3af;font-size:13px;margin:24px 0;}
  .divider::before,.divider::after{content:'';flex:1;height:1px;background:#e5e7eb;}
  .btn-outline{width:100%;padding:18px;background:#fff;color:#1e3a8a;border:2px solid #1e3a8a;
    border-radius:14px;font-size:15px;font-weight:600;text-decoration:none;display:block;
    text-align:center;}
  .foot{text-align:center;margin-top:28px;color:#6b7280;font-size:15px;}
  .foot a{color:#16a34a;font-weight:600;text-decoration:none;}
</style>
</head>
<body>
  <div class="header">
    <div class="logo">🏆</div>
    <h1>SportBooking</h1>
    <p>Reserva tu cancha favorita</p>
  </div>
  <div class="wrap">
    <h2>Bienvenido</h2>
    <p class="sub">Inicia sesión para continuar</p>
    <form onsubmit="event.preventDefault();window.location.href='/escenarios/';">
      <div class="input-group">
        <span class="icon">✉</span>
        <input type="email" placeholder="Correo electrónico" required>
      </div>
      <div class="input-group">
        <span class="icon">🔒</span>
        <input type="password" placeholder="Contraseña" required>
      </div>
      <a href="/usuarios/forgot/" class="forgot">¿Olvidaste tu contraseña?</a>
      <button class="btn" type="submit">Iniciar sesión</button>
    </form>
    <div class="divider"><span>o continúa como</span></div>
    <a href="/panel/" class="btn-outline">🛡️ Propietario / Administrador</a>
    <p class="foot">¿No tienes cuenta? <a href="/usuarios/signup/">Crear una cuenta</a></p>
  </div>
</body>
</html>
"""), name='login'),

    path('signup/', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Registro</title></head>
<body style="font-family:sans-serif;background:#f9fafb;padding:40px;text-align:center;">
  <h1 style="color:#1e3a8a;">Crear cuenta</h1>
  <p style="color:#6b7280;">Pantalla de registro.</p>
  <a href="/usuarios/" style="color:#16a34a;">← Volver al login</a>
</body></html>
"""), name='signup'),

    path('forgot/', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Recuperar</title></head>
<body style="font-family:sans-serif;background:#f9fafb;padding:40px;text-align:center;">
  <h1 style="color:#1e3a8a;">Recuperar contraseña</h1>
  <p style="color:#6b7280;">Pantalla de recuperación.</p>
  <a href="/usuarios/" style="color:#16a34a;">← Volver al login</a>
</body></html>
"""), name='forgot'),

    path('perfil/', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Mi perfil</title></head>
<body style="font-family:sans-serif;background:#f9fafb;padding:40px;text-align:center;">
  <h1 style="color:#1e3a8a;">Mi perfil</h1>
  <p style="color:#6b7280;">Datos del usuario.</p>
  <a href="/escenarios/" style="color:#16a34a;">← Volver al inicio</a>
</body></html>
"""), name='perfil'),
]