from __future__ import unicode_literals

from django.db import models

class ProductsManager(models.Manager):
    def create(self, **kwargs):
        new_product = Product(name=kwargs['post']['name'], description=kwargs['post']['description'], price=kwargs['post']['price'])
        new_product.save()
        return(True, "Product created")
    def update(self, id, **kwargs):
        update_product = Product.objects.get(id=id)
        update_product.name = kwargs['post']['name']
        update_product.description = kwargs['post']['description']
        update_product.price = kwargs['post']['price']
        update_product.save()
        return(True, "Product updated")
    def edit(self, **kwargs):
        return(True, "returned")


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductsManager()
