from django.db import models


class Solicitud(models.Model):
    vehiculos = [
        ('p', 'patineta'),
        ('b', 'bicicleta')
    ]
    tipo_de_vehiculo = models.CharField(max_length=1, choices=vehiculos, default='p')
    lugarRecogida = models.CharField(max_length=20)
    fechaRecogida = models.DateField()
    lugarEntrega = models.CharField(max_length=20)
    fechaEntrega = models.DateField()
    