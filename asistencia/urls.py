from django.urls import path

from . import views

app_name = "asistencia"

urlpatterns = [
    path("", views.formulario_asistencia, name="formulario"),
    path("confirmacion/", views.confirmacion_asistencia, name="confirmacion"),
    path("excel/<str:fecha_str>/", views.ExportarExcelPorFechaView.as_view(), name="excel_fecha"),
]
