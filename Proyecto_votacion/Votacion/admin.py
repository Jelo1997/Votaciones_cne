from django.contrib import admin

from .models import ProcesoElectoral, Candidato, Sufragante, Voto


@admin.register(ProcesoElectoral)
class ProcesoElectoralAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'fecha_inicio',
        'fecha_fin',
        'descripcion',
    )
    list_filter = ('fecha_inicio', 'fecha_fin')


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'proceso', 'nombre', 'imagen_slogan', 'imagen')
    list_filter = ('proceso',)


@admin.register(Sufragante)
class SufraganteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'cedula')


@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sufragante',
        'proceso',
        'candidato',
        'tipo_voto',
        'fecha_voto',
    )
    list_filter = ('sufragante', 'proceso', 'candidato', 'fecha_voto')