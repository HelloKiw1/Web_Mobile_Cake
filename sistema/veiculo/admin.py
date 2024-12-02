from django.contrib import admin
from veiculo.models import veiculo, evento

# Configuração para o modelo Veiculo no admin
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['id', 'marca', 'modelo', 'ano', 'cor', 'combustivel', 'foto']
    search_fields = ['modelo', 'marca']
    list_filter = ['marca', 'cor', 'combustivel']

# Configuração para o modelo Evento no admin
class EventoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'data', 'tipo']
    search_fields = ['nome']
    list_filter = ['tipo', 'data']

# Registro dos modelos no painel admin
admin.site.register(veiculo, VeiculoAdmin)
admin.site.register(evento, EventoAdmin)
