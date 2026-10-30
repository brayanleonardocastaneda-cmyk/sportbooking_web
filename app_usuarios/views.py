from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email') or request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('app_escenarios:panel_canchas')
            return redirect('app_escenarios:catalogo')
        return render(request, 'usuarios/login.html', {'error': 'Correo o contraseña incorrectos'})
    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('app_usuarios:login')


def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('email') or request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            if not Usuario.objects.filter(username=username).exists():
                user = Usuario.objects.create_user(
                    username=username,
                    email=username,
                    password=password,
                    first_name=request.POST.get('nombre', ''),
                    last_name=request.POST.get('apellido', ''),
                )
                login(request, user)
                return redirect('app_escenarios:listar_escenarios')
    return render(request, 'usuarios/registro.html')


def editar_perfil(request):
    return render(request, 'usuarios/perfil.html')


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})


@login_required
def panel_admin_view(request):
    from app_escenarios.models import Escenario
    canchas = Escenario.objects.all()
    return render(request, 'usuarios/panel_admin.html', {'canchas': canchas})
