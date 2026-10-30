from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from .models import TicketQR
from app_reservas.models import Reserva


def _staff(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(_staff)
def generar_ticket(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    ticket, created = TicketQR.objects.get_or_create(reserva=reserva, defaults={'id_ticket': f'T-{reserva.pk}'})
    if created or not ticket.codigoQR:
        ticket.generarCodigo()
    return render(request, 'app_tickets/mostrar.html', {'ticket': ticket})


@user_passes_test(_staff)
def validar_qr_view(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        try:
            ticket = TicketQR.objects.get(codigoQR=codigo)
            ya_validado = ticket.estadoValidado
            valido = ticket.validarEntrada()
            return JsonResponse({'valido': True, 'ya_validado': ya_validado})
        except TicketQR.DoesNotExist:
            return JsonResponse({'valido': False, 'mensaje': 'Ticket no encontrado'})
    return render(request, 'app_tickets/validar.html')

panel_validador = validar_qr_view
validar_ticket = validar_qr_view


@user_passes_test(_staff)
def lista_tickets(request):
    return render(request, 'app_tickets/lista.html', {'tickets': TicketQR.objects.select_related('reserva')})


@user_passes_test(_staff)
def detalle_ticket(request, pk):
    ticket = get_object_or_404(TicketQR, pk=pk)
    return render(request, 'app_tickets/detalle.html', {'ticket': ticket})


def descargar_ticket(request, pk):
    return render(request, 'app_tickets/descarga.html', {'ticket': get_object_or_404(TicketQR, pk=pk)})


def reenviar_ticket(request, pk):
    return render(request, 'app_tickets/reenviado.html', {'ticket': get_object_or_404(TicketQR, pk=pk)})
