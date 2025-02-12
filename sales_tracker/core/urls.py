from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

app_name = "core"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.novo_index, name="novo_index"),
    # URLs para cadastros e relatórios
    path("clientes/create/", views.cliente_create, name="cliente_create"),
    path("vendedores/create/", views.vendedor_create, name="vendedor_create"),
    path("produto/create/", views.produto_create, name="produto_create"),
    path("relatorios/vendas/", views.relatorio_vendas, name="relatorio_vendas"),
    path("cadastrar_venda/", views.cadastrar_venda, name="cadastrar_venda"),
    path("grupo/create/", views.grupo_create, name="grupo_create"),
    path("index/", views.index, name="index"),
    path(
        "api/vendas/",
        api_views.RelatorioVendasAPIView.as_view(),
        name="relatorio-vendas",
    ),
]
