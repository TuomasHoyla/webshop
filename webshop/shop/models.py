from __future__ import unicode_literals
from django.db import models

class Container(models.Model):

    amount = models.IntegerField(default=0)
    product = models.ForeignKey('Product', blank=True)
    
    class Meta:
        abstract = True
    
class Catalog(Container):
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.product.name


class Basket(Container):
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.product.name

    
class Product(models.Model):
    name = models.CharField(max_length=128, unique=True, default="product")
    price = models.IntegerField(default=1)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name