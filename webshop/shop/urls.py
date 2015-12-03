from django.conf.urls import include, url
from shop import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]