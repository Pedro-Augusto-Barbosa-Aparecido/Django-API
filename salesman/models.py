from django.db import models
from django.db.models import Model

# Create your models here.
from vehicle.models import Product


class Salesman(Model):
    name = models.CharField(max_length=30)
    sells = models.CharField(max_length=255, blank=True, null=True, default='R$ 00,00')
    sells_numbers = models.CharField(max_length=12, blank=True, null=True, default='0')

    class Meta:
        ordering = ("name",)
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return self.name


class Sell(Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    quantity = models.DecimalField(
        verbose_name="Quantidade solicitada desse produto",
        name="quantidade",
        max_digits=5,
        decimal_places=2
    )

    finally_price = models.CharField(max_length=255, blank=True, null=True, default='R$ 00,00')
    salesman = models.ForeignKey(Salesman, on_delete=models.PROTECT)

    class Meta:
        ordering = ("product", )
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return f'{self.product.name}, vendido pelo {self.salesman.name}'
