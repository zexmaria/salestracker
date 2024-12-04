from django.db import models
from django.core.exceptions import ValidationError


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class GrupoProduto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    grupo = models.ForeignKey(GrupoProduto, on_delete=models.CASCADE, related_name='produtos')
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - R$ {self.valor}"


class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vendas')
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='vendas')
    data_venda = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.pk:
            self.valor_total = sum(item.subtotal for item in self.itens.all())
            super().save(update_fields=['valor_total'])

    def clean(self):
        if self.pk and not self.itens.exists():
            raise ValidationError("A venda deve conter ao menos um item.")


class ItensVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    @property
    def subtotal(self):
        return self.produto.valor * self.quantidade

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.venda.save()


