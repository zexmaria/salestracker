from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'core'

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='clientes')
router.register(r'grupo-produtos', views.GrupoProdutoViewSet, basename='grupo-produtos')
router.register(r'produtos', views.ProdutoViewSet, basename='produtos')
router.register(r'vendedores', views.VendedorViewSet, basename='vendedor')
router.register(r'vendas', views.VendaViewSet, basename='vendas')
router.register(r'itens-venda', views.ItensVendaViewSet, basename='itens-venda')


urlpatterns = [
    path('', views.index, name='index'),
    path('clientes_create/', views.cliente_create, name='cliente_create'),
    path('admin/', admin.site.urls),


    # URLs para cadastros e relatórios (criar depois)
    path('clientes_create/', views.cliente_create, name='cliente_create'),
    #path('vendedores/create/', views.vendedor_create, name='vendedor_create'),
    #path('vendas/create/', views.venda_create, name='venda_create'),
    path('relatorios/vendas/', views.relatorio_vendas, name='relatorio_vendas'),
    path('cadastrar_venda/', views.cadastrar_venda, name='cadastrar_venda')
]
