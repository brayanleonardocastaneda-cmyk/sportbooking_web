from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('CLIENTE', 'Cliente'),
    )
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='CLIENTE')
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def iniciar_sesion(self, email, contrasena):
        return True # Django Auth lo maneja en la vista

    def cerrar_sesion(self):
        return True

class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50, default='Admin')

    def agregar_escenario(self, nombre, tipo, precio_hora):
        from app_escenarios.models import EscenarioDeportivo
        return EscenarioDeportivo.objects.create(nombre=nombre, tipo=tipo, precio_hora=precio_hora)

    def editar_escenario(self, id_escenario, nombre, tipo, precio_hora):
        from app_escenarios.models import EscenarioDeportivo
        escenario = EscenarioDeportivo.objects.get(id=id_escenario)
        escenario.nombre = nombre
        escenario.tipo = tipo
        escenario.precio_hora = precio_hora
        escenario.save()
        return True

    def eliminar_escenario(self, id_escenario):
        from app_escenarios.models import EscenarioDeportivo
        EscenarioDeportivo.objects.filter(id=id_escenario).delete()
        return True