from django.conf.urls import url

from . import views

app_name='Login_Store'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]