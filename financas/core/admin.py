from django.contrib import admin
from .models import TipoAtivo, CategoriaAtivo, Acao, Moeda

admin.site.register(TipoAtivo)
admin.site.register(CategoriaAtivo)
admin.site.register(Acao)
admin.site.register(Moeda)
