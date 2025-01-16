from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
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
    grupo = models.ForeignKey(
        GrupoProduto, on_delete=models.CASCADE, related_name="grupo"
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - R$ {self.valor}"


class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    registro = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="vendas"
    )
    vendedor = models.ForeignKey(
        Vendedor, on_delete=models.CASCADE, related_name="vendas"
    )
    data_venda = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    def calcular_valor_total(self):
        self.valor_total = sum(item.subtotal for item in self.itens.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ItensVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    @property
    def subtotal(self):
        return self.produto.valor * self.quantidade

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


@receiver(post_save, sender=ItensVenda)
@receiver(post_delete, sender=ItensVenda)
def atualizar_valor_total_venda(sender, instance, **kwargs):
    venda = instance.venda
    venda.valor_total = sum(item.subtotal for item in venda.itens.all())
    Venda.objects.filter(id=venda.id).update(valor_total=venda.valor_total)
