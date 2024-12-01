from django.contrib import admin
from veiculo.models import veiculo

# Register your models here.
class veiculoAdmin(admin.ModelAdmin):
    list_display = ['id', 'marca', 'modelo','ano', 'cor', 'combustivel','foto']
    search_fields = ['modelo']

admin.site.register(veiculo,veiculoAdmin)