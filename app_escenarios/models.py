from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.nombre


class Escenario(models.Model):
    DEPORTES = (
        ('futbol', 'Fútbol'), ('baloncesto', 'Baloncesto'), ('tenis', 'Tenis'),
        ('voleibol', 'Voleibol'), ('padel', 'Pádel'),
    )
    SUPERFICIES = (
        ('sintetica', 'Sintética'), ('natural', 'Natural'),
        ('cemento', 'Cemento'), ('coliseo', 'Coliseo'),
    )

    nombre = models.CharField(max_length=120)
    deporte = models.CharField(max_length=20, choices=DEPORTES)
    superficie = models.CharField(max_length=20, choices=SUPERFICIES, default='sintetica')
    precio_hora = models.DecimalField(max_digits=10, decimal_places=0)
    ubicacion = models.CharField(max_length=160)
    descripcion = models.TextField(blank=True)
    reglas = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    servicios = models.ManyToManyField(Servicio, blank=True, related_name='escenarios')
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.nombre


class ImagenEscenario(models.Model):
    escenario = models.ForeignKey(Escenario, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='escenarios/')


class Resena(models.Model):
    escenario = models.ForeignKey(Escenario, on_delete=models.CASCADE, related_name='resenas')
    usuario = models.ForeignKey('app_usuarios.Usuario', on_delete=models.CASCADE)
    calificacion = models.PositiveSmallIntegerField()
    comentario = models.TextField(blank=True)
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creada']
        unique_together = ('escenario', 'usuario')


# Compatibility with the legacy name used by older views.
EscenarioDeportivo = Escenario
