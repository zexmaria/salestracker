from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(GrupoProduto)
admin.site.register(Produto)
admin.site.register(Vendedor)
admin.site.register(Venda)
admin.site.register(ItensVenda)
