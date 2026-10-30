from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from app_escenarios.models import Escenario
from app_reservas.models import Reserva, ReservaBloque


class AppViewIntegrationTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.cliente = user_model.objects.create_user(
            username='cliente@example.com',
            email='cliente@example.com',
            password='Clave-segura-123',
        )
        self.admin = user_model.objects.create_user(
            username='admin@example.com',
            email='admin@example.com',
            password='Clave-segura-123',
            is_staff=True,
        )
        self.escenario = Escenario.objects.create(
            nombre='Cancha Central',
            deporte='futbol',
            superficie='sintetica',
            precio_hora=50000,
            ubicacion='Bogota',
        )

    def test_public_login_registration_and_scenario_pages_render(self):
        for name, args in (
            ('app_usuarios:login', []),
            ('app_usuarios:registro', []),
            ('app_escenarios:listar_escenarios', []),
            ('app_escenarios:escenario_detalle', [self.escenario.pk]),
            ('app_escenarios:horarios_disponibles', [self.escenario.pk]),
        ):
            response = self.client.get(reverse(name, args=args))
            self.assertEqual(response.status_code, 200, name)

    def test_customer_can_reserve_view_and_cancel(self):
        self.client.force_login(self.cliente)
        fecha = date.today() + timedelta(days=1)
        response = self.client.post(
            reverse('app_reservas:reservar', args=[self.escenario.pk]),
            {'fecha': fecha.isoformat(), 'bloques': ['10:00', '11:00']},
        )
        reserva = Reserva.objects.get(cliente=self.cliente, escenario=self.escenario)
        self.assertRedirects(
            response,
            reverse('app_reservas:reserva_confirmada', args=[reserva.pk]),
        )
        self.assertEqual(reserva.bloques.count(), 2)
        self.assertEqual(
            self.client.get(
                reverse('app_reservas:reserva_confirmada', args=[reserva.pk])
            ).status_code,
            200,
        )
        self.assertEqual(self.client.get(reverse('app_reservas:mis_reservas')).status_code, 200)

        response = self.client.post(
            reverse('app_reservas:reserva_cancelar', args=[reserva.pk])
        )
        self.assertRedirects(response, reverse('app_reservas:mis_reservas'))
        reserva.refresh_from_db()
        self.assertEqual(reserva.estado, 'cancelada')

    def test_customer_cannot_double_book_a_time_block(self):
        self.client.force_login(self.cliente)
        fecha = date.today() + timedelta(days=1)
        url = reverse('app_reservas:reservar', args=[self.escenario.pk])
        self.client.post(url, {'fecha': fecha.isoformat(), 'bloques': ['10:00']})

        response = self.client.post(url, {'fecha': fecha.isoformat(), 'bloques': ['10:00']})

        self.assertRedirects(
            response,
            reverse('app_escenarios:escenario_detalle', args=[self.escenario.pk]),
        )
        self.assertEqual(Reserva.objects.filter(fecha=fecha).count(), 1)
        self.assertEqual(ReservaBloque.objects.filter(hora='10:00').count(), 1)

    def test_admin_scenario_reservation_report_and_ticket_pages_render(self):
        self.client.force_login(self.admin)
        for name in (
            'app_escenarios:panel_canchas',
            'app_reservas:panel_reservas',
            'app_reportes:panel_reportes',
            'app_tickets:panel_validador',
        ):
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 200, name)

    def test_admin_can_create_scenario_and_export_reservations(self):
        self.client.force_login(self.admin)
        response = self.client.post(
            reverse('app_escenarios:cancha_crear'),
            {
                'nombre': 'Cancha Norte',
                'deporte': 'tenis',
                'superficie': 'natural',
                'precio_hora': '75000',
                'ubicacion': 'Medellin',
                'descripcion': '',
                'reglas': '',
                'servicios': [],
            },
        )
        self.assertRedirects(response, reverse('app_escenarios:panel_canchas'))
        self.assertTrue(Escenario.objects.filter(nombre='Cancha Norte').exists())

        response = self.client.get(reverse('app_reservas:reservas_exportar'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response['Content-Type'],
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )

    def test_ticket_validator_reports_unknown_code(self):
        self.client.force_login(self.admin)
        response = self.client.post(
            reverse('app_tickets:validar_ticket'),
            {'codigo': 'SB-NOEXIST'},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['valido'], False)
