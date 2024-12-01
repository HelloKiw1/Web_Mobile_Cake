from django.forms import ModelForm
from veiculo.models import veiculo

class Formularioveiculo(ModelForm):
    class Meta:
        model = veiculo
        exclude = []
    