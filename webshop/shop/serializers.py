from rest_framework import serializers

from shop.models import Product, Basket, Catalog

#serializer tuotteelle
class ProductSerializer(serializers.ModelSerializer):
    #category_name = BasketSerializer()
    
    class Meta:
        model = Product
        fields = ('name', 'price') 

#"Cannot use ModelSerializer with Abstract Models" - tasta syysta on 2 luokkaa yhden ContainerSerializer-luokan sijaan
class CatalogSerializer(ProductSerializer):
    
    item = ProductSerializer(source='product')
    
    class Meta:
        model = Catalog
        fields = ('item','amount')
        
class BasketSerializer(ProductSerializer):
    
    item = ProductSerializer(source='product')
    
    class Meta:
        model = Basket
        fields = ('item','amount')