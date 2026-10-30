from django.db import models

class ReporteReservas(models.Model):
    id_reporte = models.CharField(max_length=20, unique=True)
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    filtros_aplicados = models.CharField(max_length=255, blank=True)
    formato_exportacion = models.CharField(max_length=10) # PDF, EXCEL

    def generarReporte(self):
        # Lógica para generar el archivo
        return True