from django.shortcuts import render

import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, FormView
from django.core.validators import ValidationError
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .models import ProcesoElectoral, Candidato, Sufragante, Voto
from .forms import ProcesoElectoralForm, CandidatoForm, SufraganteForm, VotoForm, CedulaForm

# Create your views here.

def index(request):
    template = 'dashboard.html'
    c = {
        'titulo': 'ESTA ES TU CASA',
        'mensaje': 'Este es un mensaje desde la vista home'
    }
    return render(request, template, c)

def crear_proceso_electoral(request):
    if request.method == 'POST':
        form = ProcesoElectoralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_procesos_electorales')  
    else:
        form = ProcesoElectoralForm()

    return render(request, 'crear_proceso_electoral.html', {'form': form})


def lista_procesos_electorales(request):
    procesos = ProcesoElectoral.objects.all()
    return render(request, 'lista_procesos.html', {'procesos': procesos})



def agregar_candidato(request, proceso_id):
    proceso = get_object_or_404(ProcesoElectoral, pk=proceso_id)
    
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            candidato = form.save(commit=False)
            candidato.proceso = proceso
            candidato.save()
            return redirect('detalle_proceso_electoral', proceso_id=proceso.id)
    else:
        form = CandidatoForm()

    return render(request, 'agregar_candidato.html', {'form': form, 'proceso': proceso})

def registrar_sufragante(request):
    if request.method == 'POST':
        form = SufraganteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_procesos_electorales')
    else:
        form = SufraganteForm()

    return render(request, 'registrar_sufragante.html', {'form': form})

def verificar_cedula(request, proceso_id):
    proceso = get_object_or_404(ProcesoElectoral, pk=proceso_id)
    
    if request.method == 'POST':
        form = CedulaForm(request.POST)
        if form.is_valid():
            cedula = form.cleaned_data['cedula']
            try:
                sufragante = Sufragante.objects.get(cedula=cedula)
                request.session['cedula'] = sufragante.cedula  
                return redirect('detalle_proceso_electoral', proceso_id=proceso.id)  
            except Sufragante.DoesNotExist:
                form.add_error('cedula', 'Cédula no encontrada')
    else:
        form = CedulaForm()

    return render(request, 'verificar_cedula.html', {'form': form, 'proceso': proceso})

def detalle_proceso_electoral(request, proceso_id):
    proceso = get_object_or_404(ProcesoElectoral, pk=proceso_id)
    candidatos = proceso.candidatos.all()

    cedula = request.session.get('cedula')
    if not cedula:
        return redirect('verificar_cedula', proceso_id=proceso.id)

    sufragante = get_object_or_404(Sufragante, cedula=cedula)

    if request.method == 'POST':
        tipo_voto = request.POST.get('tipo_voto')  # Obtenemos el tipo de voto (blanco o nulo)
        candidato_id = request.POST.get('candidato')  # Obtenemos el id del candidato seleccionado
        
        voto = Voto(sufragante=sufragante, proceso=proceso )

        if tipo_voto in ['blanco', 'nulo']:  # Si el voto es blanco o nulo
            voto.candidato = None  # Asegurarse de que no haya candidato seleccionado
            voto.tipo_voto = tipo_voto  # Guardar el tipo de voto como blanco o nulo
        elif candidato_id:  # Si selecciona un candidato
            candidato = get_object_or_404(Candidato, pk=candidato_id)
            voto.candidato = candidato
            voto.tipo_voto = 'valido'  # Guardar como voto válido
        else:  # Si no se selecciona nada
            voto.candidato = None  # Asegurarse de que no haya candidato seleccionado
            voto.tipo_voto = 'blanco'  # Registrar como voto en blanco
        voto.save()
        
        # Cerrar la sesión del sufragante
        del request.session['cedula']  

        return redirect('verificar_cedula', proceso_id=proceso.id)

    return render(request, 'detalle_proceso.html', {
        'proceso': proceso,
        'candidatos': candidatos,
        'sufragante': sufragante
    })