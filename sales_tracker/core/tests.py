from tokenize import group
from django.db import models
from django.test import TestCase
from datetime import date
from .models import Cliente, GrupoProduto, Produto, Vendedor, Venda, ItensVenda

class CriarClienteTestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="Alice", email="alice@example.com", telefone="123456789"
        )

    def test_cliente_creation(self):
        self.assertEqual(self.cliente.nome, "Alice")
        self.assertEqual(self.cliente.email, "alice@example.com")
        self.assertEqual(self.cliente.telefone, "123456789")


class CriarVendedorTestCase(TestCase):
    def setUp(self):
        self.vendedor = Vendedor.objects.create(
            nome="Pedrinho", registro="123"
        )

    def test_vendedor_creation(self):
        self.assertEqual(self.vendedor.nome, "Pedrinho")
        self.assertEqual(self.vendedor.registro, "123")


class CriarGrupoTestCase(TestCase):
    def setUp(self):
        self.grupo = GrupoProduto.objects.create(
            nome="Eletrônicos"
        )
    def test_vendedor_creation(self):
        self.assertEqual(self.grupo.nome, "Eletrônicos")


class CriarProdutoTestCase(TestCase):
    def setUp(self):
        self.grupo = GrupoProduto.objects.create(
            nome="Eletrônicos"
        )
        self.produto = Produto.objects.create(
            nome="Celular", grupo=self.grupo,valor=1250
        )
    def test_product_creation(self):
        self.assertEqual(self.produto.nome, "Celular")
        self.assertEqual(self.produto.grupo.nome, "Eletrônicos")
        self.assertEqual(self.produto.valor, 1250)


class CriarVendaTestCase(TestCase):
        def setUp(self):
            self.cliente = Cliente.objects.create(
                nome="Alice", email="alice@example.com", telefone="123456789"
            )
            self.vendedor = Vendedor.objects.create(
                nome="Pedrinho", registro="123"
            )
            self.grupo = GrupoProduto.objects.create(
                nome="Eletrônicos"
            )
            self.venda = Venda.objects.create(
                cliente=self.cliente, vendedor=self.vendedor, data_venda=models.DateField(auto_now_add=True),
                valor_total=0
            )
            self.produto = Produto.objects.create(
                nome="Celular", grupo=self.grupo, valor=1250
            )
            self.itensvendas= ItensVenda.objects.create(
                venda=self.venda, produto=self.produto, quantidade=1
            )

        def test_venda_creation(self):
            self.assertEqual(self.venda.cliente.nome, "Alice")
            self.assertEqual(self.venda.vendedor.nome, "Pedrinho")
            self.assertEqual(self.venda.data_venda, date(2025, 1, 30))
            self.assertEqual(self.venda.valor_total, 1250)