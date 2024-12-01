from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from veiculo.models import veiculo
from veiculo.forms import Formularioveiculo
from django.urls import reverse_lazy
from veiculo.serializers import Serializaersveiculo
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions

class Listarveiculos(LoginRequiredMixin, ListView):
    model = veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class Criarveiculo(LoginRequiredMixin, CreateView):
    model = veiculo
    form_class = Formularioveiculo
    template_name = 'veiculo/criar.html'
    success_url = reverse_lazy('listar-veiculos')

class Fotoveiculo(View):
    def get(self, request, arquivo):
        try:
            veiculo = veiculo.objects.get(foto='veiculo/foto/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado!")
        except Exception as exception:
            raise exception
        return 0
        
class Editarveiculo(LoginRequiredMixin, UpdateView):
    model = veiculo
    form_class = Formularioveiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class Deletarveiculo(LoginRequiredMixin, DeleteView):
    model = veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')

class APIListarveiculos(ListAPIView):
    serializer_class = Serializaersveiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        return veiculo.objects.all()