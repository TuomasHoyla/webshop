from __future__ import unicode_literals
from django.db import models

#Abstracti container
class Container(models.Model):

    amount = models.IntegerField(default=0)
    product = models.ForeignKey('Product', blank=True)
    
    class Meta:
        abstract = True

#Katalogi, joka periytetaan abstraktista Containerista
class Catalog(Container):
#    amount = models.IntegerField(default=0)
#    product = models.ForeignKey('Product', blank=True)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.product.name

#Ostoskori, joka periytetaan abstraktista Containerista
class Basket(Container):
#    amount = models.IntegerField(default=0)
#    product = models.ForeignKey('Product', blank=True, related_name='products')
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.product.name

    
class Product(models.Model):
    name = models.CharField(max_length=128, unique=True, default="product")
    price = models.IntegerField(default=1)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

#adding/removing/editing products in Catalog & Basket
#querying products from catalog with pagination, sorting key = name/Price
#querying products from catalog, Grouping price range (5-10, < 100 etc)
#querying products from catalog, 
