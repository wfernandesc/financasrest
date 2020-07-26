from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoAtivo, CategoriaAtivo, Acao, Moeda
from .serializers import TipoAtivoSerializer, CategoriaAtivoSerializer, AcaoSerializer, MoedaSerializer


class TipoAtivoViewSet(viewsets.ModelViewSet):
    queryset = TipoAtivo.objects.all()
    serializer_class = TipoAtivoSerializer


class CategoriaAtivoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAtivo.objects.all()
    serializer_class = CategoriaAtivoSerializer


class AcaoViewSet(viewsets.ModelViewSet):
    queryset = Acao.objects.all()
    serializer_class = AcaoSerializer 
    

class MoedaViewSet(viewsets.ModelViewSet):
    queryset = Moeda.objects.all()
    serializer_class = MoedaSerializer     
