from django.conf.urls import include, url
from shop import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.myView.as_view()),
    #url(r'^products/', views.product, name='products'),
    url(r'^testview/$', views.TestView.as_view()),
    url(r'^addtobasket/', views.addToBasket, name='addtobasket'),
    #(r'^v1/(?P<variable_a>(\d+))/(?P<variable_b>(\d+))/$', r'custom1.views.v1')
    #url((r'^removefrombasket/(\d+)/(\d+)/$', views.removeFromBasket, name='addtobasket')),
    url(r'^removefrombasket/(\d+)/(\d+)/$', views.removeFromBasket, name='removefrombasket'),

    url(r'^basket/$', views.basket, name='basket'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^products/(?P<pk>[0-9]+)$', views.product_detail, name='product_detail'),
]


#If your url is something like domain/search/?q=haha, Then you would use request.GET.get('q', '').
#q is the parameter you want, And '' is the default value if q isn't found.
#If you are instead just configuring your URLconf, Then your captures from the regex are passed to the function as arguments (or named arguments).
#Such as:
#(r'^user/(?P<username>\w{0,50})/$', views.profile_page,),
#Then in your views.py you would have
#def profile_page(request, username):
    # Rest of the method