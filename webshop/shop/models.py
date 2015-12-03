from __future__ import unicode_literals

from django.db import models

class Catalog(models.Model):
    amount = models.IntegerField(default=0)
    product = models.ForeignKey('Product', blank=True)

class Basket(models.Model):
    amount = models.IntegerField(default=0)
    product = models.ForeignKey('Product', blank=True)
    

class Product(models.Model):
    
    name = models.CharField(max_length=128, unique=True, default="product")
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=1)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name


#catalog
#basket
