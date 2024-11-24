from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'grupo-produtos', GrupoProdutoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendedores', VendedorViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'itens-venda', ItensVendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
