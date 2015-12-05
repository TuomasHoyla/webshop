from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from shop.models import Product, Basket, Catalog
from django.core import serializers



def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    product_list = Product.objects.order_by('-name')[:5]
    context_dict = {'products': product_list}
    return render(request, 'shop/index.html', context_dict)

#def addToBasket(request):
#    print request
#    print "hyvin tulee"
#    return(request)

#http://stackoverflow.com/questions/30295171/django-listfield-with-add-and-remove
def addToBasket(request):
    
    value = request.GET.get('q','nada')
    olio = Product.objects.get(name=value)
    print "ajaa %d jajaj " %olio.id
    #print value
    basket_entry = Catalog.objects.get(product_id=olio.id)
    print basket_entry.amount
    basket_entry.amount = (basket_entry.amount+1)
    basket_entry.save()
    print basket_entry.amount
        
    
    product_list = Product.objects.order_by('-name')[:5]
    context_dict = {'products': product_list}
    return render(request, 'shop/index.html', context_dict)

#Myos taa onnistuu
#http://127.0.0.1:8000/shop/removefrombasket/16/2/?s='erb'&e='burn'

#search
#byname
#byamount
#https://godjango.com/41-start-your-api-django-rest-framework-part-1/
#http://www.django-rest-framework.org/api-guide/filtering/ for the user
def removeFromBasket(request, a, b):
    
    print request
    print a
    print b
    return HttpResponse(request)
#get n kpl to basket
    #katso onko catalogissa n kpl
        #jos =>n
            #lisaa n koriin
            #poista n catalogista
        #jos ei
            #palauta huono homa
        

class myView(View):
    def get(self, request):
        
        result = Product.objects.all()
        data = serializers.serialize("json", result)
        print type(data)
        return HttpResponse(data)
    

#CBV
class TestView(View):
    def get(self, request):
        greeting ="hei"
        
        return HttpResponse(greeting)

    #FBV