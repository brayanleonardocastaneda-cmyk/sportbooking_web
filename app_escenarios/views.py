from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Escenario, Servicio


def listar_escenarios(request):
    canchas = Escenario.objects.filter(activo=True)
    deporte = request.GET.get('deporte')
    if deporte:
        canchas = canchas.filter(deporte=deporte)
    return render(request, 'app_escenarios/explorar.html', {'canchas': canchas})


def explorar_canchas(request):
    return listar_escenarios(request)

catalogo = listar_escenarios


def detalle_escenario(request, pk):
    cancha = get_object_or_404(Escenario, pk=pk)
    return render(request, 'app_escenarios/detalle.html', {'cancha': cancha})

escenario_detalle = detalle_escenario
detalle_cancha = detalle_escenario


def horarios_disponibles(request, pk):
    cancha = get_object_or_404(Escenario, pk=pk)
    from datetime import time
    horas = ['07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00']
    return render(request, 'app_escenarios/detalle.html', {'cancha': cancha, 'horarios': horas})


@login_required
def panel_canchas(request):
    return render(request, 'panel_admin.html', {'canchas': Escenario.objects.all()})

lista_escenarios_admin = panel_canchas


@login_required
def crear_escenario(request):
    if request.method == 'POST':
        escenario = Escenario.objects.create(
            nombre=request.POST.get('nombre', ''), deporte=request.POST.get('deporte', 'futbol'),
            superficie=request.POST.get('superficie', 'sintetica'), precio_hora=request.POST.get('precio_hora', 0),
            ubicacion=request.POST.get('ubicacion', ''), descripcion=request.POST.get('descripcion', ''),
            reglas=request.POST.get('reglas', ''), activo=True,
        )
        servicio_ids = request.POST.getlist('servicios')
        if servicio_ids:
            escenario.servicios.set(servicio_ids)
        return redirect('app_escenarios:panel_canchas')
    return render(request, 'app_escenarios/crear.html')


@login_required
def editar_escenario(request, pk):
    cancha = get_object_or_404(Escenario, pk=pk)
    if request.method == 'POST':
        for field in ('nombre', 'deporte', 'superficie', 'precio_hora', 'ubicacion', 'descripcion', 'reglas'):
            if field in request.POST:
                setattr(cancha, field, request.POST[field])
        cancha.save()
        return redirect('app_escenarios:panel_canchas')
    return render(request, 'app_escenarios/editar.html', {'cancha': cancha})


@login_required
def eliminar_escenario(request, pk):
    get_object_or_404(Escenario, pk=pk).delete()
    return redirect('app_escenarios:panel_canchas')
