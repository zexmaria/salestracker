from django.test import TestCase
from .models import Cliente, GrupoProduto, Produto, Vendedor, Venda, ItensVenda

class ClienteTestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="Alice", email="alice@example.com", telefone="123456789"
        )

    def test_cliente_creation(self):
        self.assertEqual(self.cliente.nome, "Alice")
        self.assertEqual(self.cliente.email, "alice@example.com")
        self.assertEqual(self.cliente.telefone, "123456789")
