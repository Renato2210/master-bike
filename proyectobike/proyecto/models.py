# Create your models here.

from django.db import models

class Pago(models.Model):
    METODOS_ENTREGA = [
        ('envio', 'Envío'),
        ('tienda', 'Retiro en tienda'),
    ]

    nombre = models.CharField(max_length=100)
    numero_tarjeta = models.CharField(max_length=16)
    fecha_vencimiento = models.CharField(max_length=5)
    metodo_entrega = models.CharField(max_length=6, choices=METODOS_ENTREGA)

    def __str__(self):
        return f'{self.nombre} - {self.numero_tarjeta}'

