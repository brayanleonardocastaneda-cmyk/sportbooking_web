from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.db import transaction
from datetime import datetime
from app_escenarios.models import Escenario
from .models import Reserva, ReservaBloque


@login_required
def panel_reservas(request):
    reservas = Reserva.objects.select_related('cliente', 'escenario').order_by('-creada')
    return render(request, 'app_reservas/admin_lista.html', {'reservas': reservas})

lista_reservas_admin = panel_reservas


@login_required
def reservar(request, cancha_id):
    cancha = get_object_or_404(Escenario, pk=cancha_id)
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        horas = request.POST.getlist('bloques')
        if fecha and horas:
            existente = ReservaBloque.objects.filter(
                reserva__escenario=cancha, reserva__fecha=fecha, reserva__estado='activa', hora__in=horas
            ).exists()
            if not existente:
                reserva = Reserva.objects.create(cliente=request.user, escenario=cancha, fecha=fecha, estado='activa')
                ReservaBloque.objects.bulk_create([
                    ReservaBloque(reserva=reserva, hora=datetime.strptime(hora, '%H:%M').time()) for hora in horas
                ])
                return redirect('app_reservas:reserva_confirmada', reserva.pk)
            return redirect('app_escenarios:escenario_detalle', cancha.pk)
    return render(request, 'app_reservas/crear.html', {'cancha': cancha})

crear_reserva = reservar


@login_required
def reserva_confirmada(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk, cliente=request.user)
    return render(request, 'app_reservas/confirmacion.html', {'reserva': reserva})


@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(cliente=request.user).select_related('escenario').order_by('-creada')
    return render(request, 'app_reservas/mis_reservas.html', {'reservas': reservas})


@login_required
def reserva_cancelar(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk, cliente=request.user)
    reserva.cancelar()
    return redirect('app_reservas:mis_reservas')

cancelar_reserva = reserva_cancelar


@login_required
def completar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.estado = 'completada'
    reserva.save(update_fields=['estado'])
    return redirect('app_reservas:panel_reservas')


@login_required
def reservas_exportar(request):
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    ws.append(['Cliente', 'Escenario', 'Fecha', 'Estado'])
    for reserva in Reserva.objects.select_related('cliente', 'escenario'):
        ws.append([reserva.cliente.username, reserva.escenario.nombre, reserva.fecha.isoformat(), reserva.estado])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="reservas.xlsx"'
    wb.save(response)
    return response


def detalle_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'app_reservas/detalle.html', {'reserva': reserva})
