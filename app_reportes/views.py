import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Sum
from app_reservas.models import Reserva
from app_escenarios.models import Escenario


def _staff(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(_staff)
def panel_reportes(request):
    reservas = Reserva.objects.select_related('escenario')
    ingresos_totales = sum((escenario.precio_hora for reserva in reservas for escenario in [reserva.escenario]), 0)
    ocupacion = reservas.count()
    horas_pico = list(reservas.values('bloques__hora').annotate(total=Count('id')).order_by('-total')[:5])
    horas_pico_json = json.dumps([{'hora': str(x['bloques__hora']), 'total': x['total']} for x in horas_pico])
    ingresos_por_cancha = [{'nombre': e.nombre, 'total': float(e.precio_hora) * e.reservas.count()} for e in Escenario.objects.all()]
    context = {
        'ingresos_totales': ingresos_totales,
        'horas_vendidas': sum(r.bloques.count() for r in reservas),
        'ocupacion': ocupacion,
        'horas_pico_json': horas_pico_json,
        'ingresos_por_cancha_json': json.dumps(ingresos_por_cancha),
    }
    return render(request, 'app_reportes/reportes.html', context)


@user_passes_test(_staff)
def exportar_excel(request):
    from django.http import HttpResponse
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    ws.append(['Reserva', 'Escenario', 'Fecha', 'Estado'])
    for reserva in Reserva.objects.select_related('escenario'):
        ws.append([reserva.pk, reserva.escenario.nombre, reserva.fecha.isoformat(), reserva.estado])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="reportes.xlsx"'
    wb.save(response)
    return response


exportar_pdf = panel_reportes
reporte_reservas = panel_reportes
generar_reporte_filtrado = panel_reportes


@user_passes_test(_staff)
def detalle_reporte(request, pk):
    return render(request, 'app_reportes/reportes.html', {'report_id': pk})
