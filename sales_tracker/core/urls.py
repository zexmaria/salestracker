from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes_create/', views.cliente_create, name='cliente_create'),
    path('admin/', admin.site.urls),

    # URLs para cadastros e relatórios
    path('clientes/create/', views.cliente_create, name='cliente_create'),
    path('vendedores/create/', views.vendedor_create, name='vendedor_create'),
    path('produto/create/', views.cadastrar_venda, name='produto_create'),
    path('relatorios/vendas/', views.relatorio_vendas, name='relatorio_vendas'),
    path('cadastrar_venda/', views.cadastrar_venda, name='cadastrar_venda'),
    path('api/vendas/', api_views.RelatorioVendasAPIView.as_view(), name='relatorio-vendas'),

]
