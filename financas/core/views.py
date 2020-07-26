#  django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Acao, CategoriaAtivo, Moeda, TipoAtivo
from .serializers import (AcaoSerializer, CategoriaAtivoSerializer,
                          MoedaSerializer, TipoAtivoSerializer)


class TipoAtivoViewSet(viewsets.ModelViewSet):
    queryset = TipoAtivo.objects.all()
    serializer_class = TipoAtivoSerializer
    permission_classes = (IsAuthenticated, )


class CategoriaAtivoFilterSet(filters.FilterSet):
   missing = filters.BooleanFilter(field_name='returned', lookup_expr='isnull')
   # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
   # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

   class Meta:
       model = CategoriaAtivo
       fields = ['nome']


class CategoriaAtivoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAtivo.objects.all()
    serializer_class = CategoriaAtivoSerializer
    permission_classes = (IsAuthenticated, )
    filterset_class = CategoriaAtivoFilterSet
     

class AcaoViewSet(viewsets.ModelViewSet):
    queryset = Acao.objects.all()
    serializer_class = AcaoSerializer
    permission_classes = (IsAuthenticated, )



class MoedaViewSet(viewsets.ModelViewSet):
    queryset = Moeda.objects.all()
    serializer_class = MoedaSerializer
    permission_classes = (IsAuthenticated, )
