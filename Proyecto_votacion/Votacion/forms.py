from .models import *
from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit

from .models import ProcesoElectoral, Candidato, Sufragante, Voto

class ProcesoElectoralForm(forms.ModelForm):
    class Meta:
        model = ProcesoElectoral
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'descripcion']

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nombre', 'imagen_slogan', 'imagen']


class SufraganteForm(forms.ModelForm):
    class Meta:
        model = Sufragante
        fields = ['nombre', 'apellido', 'cedula']


class VotoForm(forms.ModelForm):
    sufragante_id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Voto
        fields = ['sufragante_id', 'candidato']

    def __init__(self, *args, **kwargs):
        proceso = kwargs.pop('proceso', None)  # Recibir el proceso desde la vista
        super(VotoForm, self).__init__(*args, **kwargs)

        if proceso:
            # Mostrar los candidatos como opciones de radio
            self.fields['candidato'].queryset = Candidato.objects.filter(proceso=proceso)
            self.fields['candidato'].widget = forms.RadioSelect()  # Usar RadioSelect para candidatos

class CedulaForm(forms.Form):
    cedula = forms.CharField(max_length=20, label='Cédula')