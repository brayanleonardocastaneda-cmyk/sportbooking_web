from django.db import models
from app_reservas.models import Reserva
import qrcode
from io import BytesIO
from django.core.files import File

class TicketQR(models.Model):
    id_ticket = models.CharField(max_length=20, unique=True)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    codigoQR = models.CharField(max_length=100, blank=True, default='')
    fechaEmision = models.DateTimeField(auto_now_add=True)
    estadoValidado = models.BooleanField(default=False)

    def generarCodigo(self):
        self.codigoQR = f"SB-{self.reserva.pk}"
        qrcode.make(self.codigoQR)
        self.save(update_fields=['codigoQR'])

    def validarEntrada(self):
        if not self.estadoValidado:
            self.estadoValidado = True
            self.save()
            return True
        return False