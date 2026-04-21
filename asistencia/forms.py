from django import forms

from .models import RegistroAsistencia


class RegistroAsistenciaForm(forms.ModelForm):
    class Meta:
        model = RegistroAsistencia
        fields = ["dni", "apellido", "nombre"]
        widgets = {
            "dni": forms.TextInput(
                attrs={
                    "class": "input",
                    "autocomplete": "off",
                    "inputmode": "numeric",
                    "pattern": r"[0-9]+",
                }
            ),
            "apellido": forms.TextInput(attrs={"class": "input", "autocomplete": "family-name"}),
            "nombre": forms.TextInput(attrs={"class": "input", "autocomplete": "given-name"}),
        }

    def clean_dni(self):
        dni = self.cleaned_data["dni"].strip()
        if not dni.isdigit():
            raise forms.ValidationError("El DNI solo puede contener numeros.")
        return dni
