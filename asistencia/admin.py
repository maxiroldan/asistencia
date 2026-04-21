from django.contrib import admin

from .models import RegistroAsistencia


@admin.register(RegistroAsistencia)
class RegistroAsistenciaAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "dni", "fecha")
    list_filter = ("fecha",)
    search_fields = ("dni", "nombre", "apellido")
