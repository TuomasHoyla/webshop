from django.conf.urls import include, url
from shop import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.myView.as_view()),
    #url(r'^products/', views.product, name='products'),
    url(r'^testview/$', views.TestView.as_view()),
]