from django.db import models


class RegistroAsistencia(models.Model):
    dni = models.CharField("DNI", max_length=20)
    nombre = models.CharField("Nombre", max_length=100)
    apellido = models.CharField("Apellido", max_length=100)
    fecha = models.DateField("Fecha de asistencia")

    class Meta:
        ordering = ["-fecha", "apellido", "nombre"]
        verbose_name = "registro de asistencia"
        verbose_name_plural = "registros de asistencia"

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.fecha})"
