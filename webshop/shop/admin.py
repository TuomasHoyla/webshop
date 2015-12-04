from django.contrib import admin
from models import Catalog, Basket, Product

# Register your models here.
admin.site.register(Catalog)
admin.site.register(Basket)
admin.site.register(Product)
#admin.site.register(Container)