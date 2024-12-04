from rest_framework import viewsets
from .models import Cliente, GrupoProduto, Produto, Vendedor, Venda, ItensVenda
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect



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


def index(request):
    context = {
        'clientes': Cliente.objects.all(),
        'vendedores': Vendedor.objects.all()
    }
    return render(request, 'core/index.html', context)


def relatorio_vendas(request):
    vendas = Venda.objects.all()

    # Filtros opcionais
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    vendedor = request.GET.get('vendedor')
    cliente = request.GET.get('cliente')

    if data_inicio:
        vendas = vendas.filter(data__gte=data_inicio)
    if data_fim:
        vendas = vendas.filter(data__lte=data_fim)
    if vendedor:
        vendas = vendas.filter(vendedor_id=vendedor)
    if cliente:
        vendas = vendas.filter(cliente_id=cliente)

    context = {
        'vendas': vendas
    }
    return render(request, 'core/relatorio_vendas.html', context)


def cliente_create(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        Cliente.objects.create(nome=nome, email=email, telefone=telefone)

        return redirect('/')

    return render(request, 'core/cliente_create.html')


def cadastrar_venda(request):
    if request.method == "POST":
        cliente_id = request.POST.get("cliente")
        vendedor_id = request.POST.get("vendedor")
        produtos = request.POST.getlist("produtos[]")
        quantidades = request.POST.getlist("quantidades[]")

        cliente = Cliente.objects.get(id=cliente_id)
        vendedor = Vendedor.objects.get(id=vendedor_id)
        venda = Venda.objects.create(cliente=cliente, vendedor=vendedor)

        for produto_id, quantidade in zip(produtos, quantidades):
            if not quantidade or int(quantidade) <= 0:
                continue
            produto = Produto.objects.get(id=produto_id)
            ItensVenda.objects.create(venda=venda, produto=produto, quantidade=int(quantidade))
            return render(request, "core/cadastrar_venda.html")

    clientes = Cliente.objects.all()
    vendedores = Vendedor.objects.all()
    produtos = Produto.objects.all()
    return render(request, "core/cadastrar_venda.html", {
        "clientes": clientes,
        "vendedores": vendedores,
        "produtos": produtos,
    })
