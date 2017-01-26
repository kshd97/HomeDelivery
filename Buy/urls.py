from django.conf.urls import url

from . import views

app_name='Buy'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Category_Shop', views.Category_Shop, name='Category_Shop'),
    url(r'^Category/(?P<cat>[A-Za-z]+)/$', views.Category, name='Category'),
    url(r'^Category/(?P<cat>[A-Za-z]+)/Item/(?P<item>[A-Za-z]+)/$', views.Item, name='Item'),
]