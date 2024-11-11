from django.shortcuts import render
import openpyxl
import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, FormView
from django.core.validators import ValidationError
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from .decorators import login_required_and_staff
from django.template.loader import render_to_string
from django.utils import timezone
import matplotlib.pyplot as plt
import base64

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

@login_required_and_staff
def crear_proceso_electoral(request):
    if request.method == 'POST':
        form = ProcesoElectoralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_procesos_electorales')
    else:
        form = ProcesoElectoralForm()

    return render(request, 'crear_proceso_electoral.html', {'form': form})

@login_required
def lista_procesos_electorales(request):
    procesos = ProcesoElectoral.objects.all()
    return render(request, 'lista_procesos.html', {'procesos': procesos})


@login_required_and_staff
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

@login_required_and_staff
def registrar_sufragante(request, proceso_id):
    proceso = get_object_or_404(ProcesoElectoral, pk=proceso_id)

    if request.method == 'POST':
        archivo_excel = request.FILES.get('archivo_excel')

        if archivo_excel:
            try:
                workbook = openpyxl.load_workbook(archivo_excel)
                sheet = workbook.active

                # Iterar sobre las filas del archivo Excel (nombre, apellido, cédula, curso)
                for row in sheet.iter_rows(min_row=2, values_only=True):
                    nombre, apellido, cedula, curso = row  # Asegúrate de que la columna de curso esté en el Excel

                    # Verificar si el sufragante ya está registrado por cédula
                    if not Sufragante.objects.filter(cedula=cedula).exists():
                        # Crear el sufragante y asociarlo al proceso y al curso
                        Sufragante.objects.create(
                            nombre=nombre,
                            apellido=apellido,
                            cedula=cedula,
                            proceso=proceso,  # Relacionar con el proceso actual
                            curso=curso  # Registrar el curso
                        )
                
                return redirect('lista_procesos_electorales')

            except Exception as e:
                return render(request, 'registrar_sufragante.html', {
                    'error': 'Error al procesar el archivo. Verifique el formato.',
                    'proceso': proceso
                })
    
    return render(request, 'registrar_sufragante.html', {'proceso': proceso})

@login_required
def verificar_cedula(request, proceso_id):
    proceso = get_object_or_404(ProcesoElectoral, pk=proceso_id)
    mensaje = None  

    if request.method == 'POST':
        form = CedulaForm(request.POST)
        if form.is_valid():
            cedula = form.cleaned_data['cedula']
            try:
                sufragante = Sufragante.objects.get(cedula=cedula)
                
                
                if Voto.objects.filter(sufragante=sufragante, proceso=proceso).exists():
                    mensaje = 'La cédula {} ya ha registrado un voto en este proceso electoral. No puedes votar nuevamente.'.format(sufragante.cedula)
                else:
                    request.session['cedula'] = sufragante.cedula  
                    return redirect('detalle_proceso_electoral', proceso_id=proceso.id)  
            except Sufragante.DoesNotExist:
                form.add_error('cedula', 'Cédula no encontrada')
    else:
        form = CedulaForm()

    return render(request, 'verificar_cedula.html', {
        'form': form,
        'proceso': proceso,
        'mensaje': mensaje,  
    })

@login_required
def detalle_proceso_electoral(request, proceso_id):
    proceso = get_object_or_404(ProcesoElectoral, pk=proceso_id)
    candidatos = proceso.candidatos.all()

    cedula = request.session.get('cedula')
    if not cedula:
        return redirect('verificar_cedula', proceso_id=proceso.id)

    sufragante = get_object_or_404(Sufragante, cedula=cedula)

    if request.method == 'POST':
        candidato_id = request.POST.get('candidato')
        
        voto = Voto(sufragante=sufragante, proceso=proceso)
        if candidato_id:  
            candidato = get_object_or_404(Candidato, pk=candidato_id)
            voto.candidato = candidato
            voto.tipo_voto = 'valido'
        voto.save()

        del request.session['cedula']
        return redirect('verificar_cedula', proceso_id=proceso.id)

    return render(request, 'detalle_proceso.html', {'proceso': proceso, 'candidatos': candidatos, 'sufragante': sufragante,'curso': sufragante.curso})

@login_required_and_staff
def resultados_votacion(request, proceso_id):
    proceso = ProcesoElectoral.objects.get(id=proceso_id)
    resultados = {}
    total_votos = Voto.objects.filter(proceso=proceso)

    for candidato in proceso.candidatos.all():
        resultados[candidato] = total_votos.filter(candidato=candidato).count()

    total_sufragantes = total_votos.values('sufragante').distinct().count()
    fecha_generacion = timezone.now().strftime('%d de %B de %Y')

    context = {
        'proceso': proceso,
        'resultados': resultados,
        'total_sufragantes': total_sufragantes,
        'fecha_generacion': fecha_generacion,
    }

    return render(request, 'resultados.html', context)

@login_required_and_staff
def resultados_pdf(request, proceso_id):
    # Obtener el proceso y los candidatos
    proceso = get_object_or_404(ProcesoElectoral, id=proceso_id)
    candidatos = Candidato.objects.filter(proceso=proceso)
    votos = Voto.objects.filter(proceso=proceso)

    # Inicializar diccionario de resultados
    resultados = {}
    total_votos_validos = 0

    # Contar votos por candidato
    for candidato in candidatos:
        votos_validos = votos.filter(candidato=candidato, tipo_voto='valido').count()
        resultados[candidato] = {
            'votos': votos_validos,
            'porcentaje': 0  # Inicializar porcentaje
        }
        total_votos_validos += votos_validos

    # Contar votos en blanco y nulos
    votos_blanco = votos.filter(tipo_voto='blanco').count()
    votos_nulo = votos.filter(tipo_voto='nulo').count()

    # Calcular el total de votos emitidos
    total_votos_emitidos = total_votos_validos + votos_blanco + votos_nulo
    total_sufragantes = total_votos_emitidos
    total_sufragantes_registrados = Sufragante.objects.count()
    no_sufragantes = total_sufragantes_registrados - total_votos_emitidos

    # Calcular porcentajes para cada candidato
    for candidato, data in resultados.items():
        if total_votos_emitidos > 0:
            data['porcentaje'] = (data['votos'] / total_votos_emitidos) * 100

    # Calcular porcentajes de votos en blanco, nulos y no sufragantes
    porcentaje_blanco = (votos_blanco / total_votos_emitidos) * 100 if total_votos_emitidos > 0 else 0
    porcentaje_nulo = (votos_nulo / total_votos_emitidos) * 100 if total_votos_emitidos > 0 else 0
    porcentaje_no_sufragantes = (no_sufragantes / total_sufragantes_registrados) * 100 if total_sufragantes_registrados > 0 else 0

    # Generar gráfico con Matplotlib
    fig, ax = plt.subplots(figsize=(4, 3))
    labels = [candidato.nombre for candidato in candidatos] 
    votos_data = [data['votos'] for data in resultados.values()]

    ax.bar(labels, votos_data, color=['#007bff', '#28a745', '#dc3545'])  # Colores para barras
    ax.set_ylabel('Votos')
    ax.set_title('Resultados de Votación')

    # Guardar el gráfico en un buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)

    # Codificar la imagen en base64
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    image_uri = 'data:image/png;base64,' + image_base64

    # Preparar el contexto
    context = {
        'proceso': proceso,
        'resultados': resultados,
        'porcentaje_blanco': round(porcentaje_blanco, 2),
        'porcentaje_nulo': round(porcentaje_nulo, 2),
        'no_sufragantes': no_sufragantes,
        'porcentaje_no_sufragantes': round(porcentaje_no_sufragantes, 2),
        'total_sufragantes': total_sufragantes,
        'fecha_generacion': timezone.now(),
        'image_uri': image_uri,  # Incluir la URI de la imagen en el contexto
    }

    # Renderizar la plantilla y generar el PDF
    template = get_template('resultados_pdf.html')
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resultados_{proceso.nombre}.pdf"'
    pisa_status = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), dest=response)

    if pisa_status.err:
        return HttpResponse(f'Error al generar PDF: {pisa_status.err}', content_type='text/plain')

    return response


@login_required_and_staff
def generar_pdf_padron(request, proceso_id):
    proceso = ProcesoElectoral.objects.get(id=proceso_id)
    sufragantes = Sufragante.objects.all()

    # Diccionarios para agrupar votantes y no votantes por curso
    votantes_por_curso = {}
    no_votantes_por_curso = {}

    for sufragante in sufragantes:
        # Obtener el curso del sufragante
        curso = sufragante.curso

        # Verificar si el sufragante ha votado
        if Voto.objects.filter(sufragante=sufragante, proceso=proceso).exists():
            if curso not in votantes_por_curso:
                votantes_por_curso[curso] = []
            votantes_por_curso[curso].append(sufragante)
        else:
            if curso not in no_votantes_por_curso:
                no_votantes_por_curso[curso] = []
            no_votantes_por_curso[curso].append(sufragante)

    # Preparar el contexto con los datos agrupados
    context = {
        'votantes_por_curso': votantes_por_curso,
        'no_votantes_por_curso': no_votantes_por_curso,
        'proceso': proceso
    }

    # Renderizar el template y generar el PDF
    html = render_to_string('padron_electoral.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=padron_electoral_{proceso_id}.pdf'
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF.')
    return response


@login_required_and_staff
def reiniciar_votacion(request, proceso_id):
    proceso = get_object_or_404(ProcesoElectoral, id=proceso_id)
    
    Voto.objects.filter(proceso=proceso).delete()
    
    return redirect('resultados_votacion', proceso_id=proceso.id)

    