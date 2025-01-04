from django.contrib import admin
from .models import *


class ItensVendaInline(admin.TabularInline):
    model = ItensVenda
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    inlines = [ItensVendaInline]  # Relaciona os itens de venda à venda principal
    list_display = ["cliente", "vendedor", "data_venda", "valor_total", "inlines"]


admin.site.register(Cliente)
admin.site.register(GrupoProduto)
admin.site.register(Produto)
admin.site.register(Vendedor)
admin.site.register(Venda, VendaAdmin)
