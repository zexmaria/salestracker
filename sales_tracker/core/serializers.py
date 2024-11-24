from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class GrupoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoProduto
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'


class ItensVendaSerializer(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = ItensVenda
        fields = '__all__'


class VendaSerializer(serializers.ModelSerializer):
    itens = ItensVendaSerializer(many=True, read_only=True)
    valor_total = serializers.ReadOnlyField()

    class Meta:
        model = Venda
        fields = '__all__'
