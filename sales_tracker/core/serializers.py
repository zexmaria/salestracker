from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class GrupoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoProduto
        fields = "__all__"

"""
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
"""

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"


"""
class ItensVendaSerializer(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = ItensVenda
        fields = "__all__"

"""


class ProdutoSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='nome', read_only=True)

    class Meta:
        model = Produto
        fields = ['nome', 'quantidade']

class ItensVendaSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)

    class Meta:
        model = ItensVenda
        fields = ['produto_nome', 'quantidade']

class VendaSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    vendedor_nome = serializers.CharField(source='vendedor.nome', read_only=True)
    produtos = ItensVendaSerializer(source='itens', many=True)

    class Meta:
        model = Venda
        fields = "__all__"

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        venda = Venda.objects.create(**validated_data)
        for item_data in itens_data:
            ItensVenda.objects.create(venda=venda, **item_data)
        venda.calcular_valor_total()
        venda.save(update_fields=["valor_total"])
        return venda
