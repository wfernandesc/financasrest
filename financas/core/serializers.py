from rest_framework import serializers
from .models import TipoAtivo, CategoriaAtivo, Acao, Moeda

class TipoAtivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoAtivo
        fields = ['nome']


class CategoriaAtivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoriaAtivo
        fields = '__all__'


class AcaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Acao
        fields = ['codigo', 'ultimaCotacao', 'peso', 'quantidade', 'categoria', 'valorTotal', 'percIdeal', 'percPosse', 'moeda']


class MoedaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Moeda
        fields = '__all__'      