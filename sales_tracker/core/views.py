from rest_framework import viewsets
from .models import Cliente, GrupoProduto, Produto, Vendedor, Venda, ItensVenda
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render



class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class GrupoProdutoViewSet(viewsets.ModelViewSet):
    queryset = GrupoProduto.objects.all()
    serializer_class = GrupoProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    @action(detail=False, methods=['get'])
    def relatorio(self, request):
        cliente_id = request.query_params.get('cliente')
        vendedor_id = request.query_params.get('vendedor')
        data = request.query_params.get('data')

        vendas = self.queryset
        if cliente_id:
            vendas = vendas.filter(cliente_id=cliente_id)
        if vendedor_id:
            vendas = vendas.filter(vendedor_id=vendedor_id)
        if data:
            vendas = vendas.filter(data_venda=data)

        serializer = self.get_serializer(vendas, many=True)
        return Response(serializer.data)


class ItensVendaViewSet(viewsets.ModelViewSet):
    queryset = ItensVenda.objects.all()
    serializer_class = ItensVendaSerializer



# Create your views here.
