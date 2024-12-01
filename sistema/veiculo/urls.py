from django.urls import path
from veiculo.views import Listarveiculos, Fotoveiculo, Criarveiculo, Editarveiculo, Deletarveiculo, APIListarveiculos

urlpatterns = [
    path('', Listarveiculos.as_view(), name='listar-veiculos'),
    path('novo/', Criarveiculo.as_view(), name = 'criar-veiculos'),
    path('<int:pk>/', Editarveiculo.as_view(), name = 'editar-veiculos'),
    path('deletar/<int:pk>/', Deletarveiculo.as_view(), name = 'deletar-veiculos'),
    path('foto/<str:arquivo>/', Fotoveiculo.as_view(), name='foto-veiculo'),
    path('api/', APIListarveiculos.as_view(),name='api-listar-veiculos')
]