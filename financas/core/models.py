# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
from django.db import models


class TipoAtivo(models.Model):

    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class CategoriaAtivo(models.Model):
    nome = models.CharField(max_length=20)
    tipo = models.ForeignKey(TipoAtivo, on_delete=models.CASCADE, null=False, verbose_name='Tipo Ativo')

    def __str__(self):
        return self.nome


class Moeda(models.Model):
    codigo = models.CharField(max_length=3)
    descricao = models.TextField(max_length=50, default='BRL')
    ultimaCotacao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Cotação')
    dataUltimaCotacao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.codigo

class Acao(models.Model):
    codigo = models.CharField(max_length=10, unique=True, verbose_name='Código')
    ultimaCotacao = models.DecimalField(max_digits=10, decimal_places=2,
                                        null=True, blank=True, verbose_name='Cotação')
    peso = models.IntegerField(verbose_name='Peso')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    categoria = models.ForeignKey(CategoriaAtivo, on_delete=models.CASCADE, null=False, verbose_name='Categoria')
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Valor Total')
    percIdeal = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='% Ideal')
    percPosse = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='% Posse')
    moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE, null=False, verbose_name='Moeda')

    class Meta:
        verbose_name_plural = 'Acoes'

    def __str__(self):
        return self.codigo


# class Receita(models.Model):
#    pass
