from django.db import models
from django.db.models import Model

# Create your models here.
from vehicle.models import Product


class Salesman(Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ("name",)
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return self.name

    @property
    def attribute(self):
        return {
            "name": self.name,
            "id": self.pk
        }


class Sell(Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    quantity = models.CharField(max_length=10, blank=False, null=True, verbose_name="Quantidade")

    finally_price = models.CharField(max_length=255, blank=True, null=True, default='R$ 00,00')
    salesman = models.ForeignKey(Salesman, on_delete=models.PROTECT)

    class Meta:
        ordering = ("product", )
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return f'{self.product.name}, vendido pelo {self.salesman.name}'

    @staticmethod
    def get_price(price):
        price = price[price.find('$') + 2:]
        price = price.replace(',', '.')
        return float(price)

    @property
    def attribute(self):
        return {
            "product": self.product.attributes,
            "salesman": self.salesman.attribute,
            "quantity": self.quantity,
            "finally_price": self.finally_price
        }
