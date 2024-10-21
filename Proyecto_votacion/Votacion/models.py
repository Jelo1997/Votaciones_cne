from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from django.utils import timezone
# Create your models here.


class ProcesoElectoral(models.Model):
    nombre = models.CharField(max_length=255)  
    fecha_inicio = models.DateField()  
    fecha_fin = models.DateField()  
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre


class Candidato(models.Model):
    proceso = models.ForeignKey(ProcesoElectoral, on_delete=models.CASCADE, related_name='candidatos')
    nombre = models.CharField(max_length=255)  
    slogan = models.CharField(max_length=255)  
    imagen = models.ImageField(upload_to='imagenes_candidatos/')  

    def __str__(self):
        return self.nombre


class Sufragante(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cedula = models.CharField(max_length=20, unique=True)  #única para identificar al votante

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cedula}"


class Voto(models.Model):
    TIPOS_VOTO = (
        ('valido', 'Válido'),
        ('blanco', 'Blanco'),
        ('nulo', 'Nulo'),
    )

    sufragante = models.ForeignKey(Sufragante, on_delete=models.CASCADE, related_name='votos')  
    proceso = models.ForeignKey(ProcesoElectoral, on_delete=models.CASCADE, related_name='votos')  
    candidato = models.ForeignKey(Candidato, null=True, blank=True, on_delete=models.SET_NULL, related_name='votos')  
    tipo_voto = models.CharField(max_length=10, choices=TIPOS_VOTO, blank=True)  
    fecha_voto = models.DateTimeField(default=timezone.now) 
    def clean(self):
        
        if self.candidato and self.tipo_voto != 'valido':
            raise ValidationError('Debe ser un voto válido si selecciona un candidato.')
        
        if not self.candidato and self.tipo_voto == 'valido':
            raise ValidationError('Debe seleccionar un candidato para un voto válido.')

    def __str__(self):
        if self.tipo_voto == 'valido' and self.candidato:
            return f"Voto válido por {self.candidato.nombre}"
        else:
            return f"Voto {self.get_tipo_voto_display()}"