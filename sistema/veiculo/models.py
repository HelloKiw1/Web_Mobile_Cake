from django.db import models
from datetime import datetime
from veiculo.consts import *

class veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    foto = models.ImageField(blank=True, null=True, upload_to='veiculo/foto')
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(
            self.get_marca_display(),
            self.modelo,
            self.ano,
            self.get_cor_display()
        )

    def anos_de_uso(self):
        """Retorna o número de anos de uso do veículo."""
        return datetime.now().year - self.ano

    @property
    def veiculo_novo(self):
        """Verifica se o veículo é do ano atual."""
        return self.ano == datetime.now().year


class evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    tipo = models.SmallIntegerField(choices=OPCOES_TIPOS_EVENTOS)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()}) - {self.data.strftime('%d/%m/%Y')}"

    @property
    def evento_passado(self):
        """Verifica se o evento já aconteceu."""
        return self.data < datetime.now().date()

    @property
    def dias_para_evento(self):
        """Calcula o número de dias restantes até o evento."""
        delta = (self.data - datetime.now().date()).days
        return delta if delta > 0 else 0
