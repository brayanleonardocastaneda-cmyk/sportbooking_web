from django.db import models
from django.conf import settings
from app_escenarios.models import Escenario


class Reserva(models.Model):
    ESTADOS = (
        ('activa', 'Activa'), ('cancelada', 'Cancelada'), ('completada', 'Completada'),
    )
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservas')
    escenario = models.ForeignKey(Escenario, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activa')
    creada = models.DateTimeField(auto_now_add=True)

    def cancelar(self):
        self.estado = 'cancelada'
        self.save(update_fields=['estado'])
        return True


class ReservaBloque(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='bloques')
    hora = models.TimeField()

    class Meta:
        unique_together = ('reserva', 'hora')
