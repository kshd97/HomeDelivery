from django.conf.urls import url

from . import views

app_name='Login'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Signin', views.Signin, name='Signin'),
    url(r'^Signup', views.Signup, name='Signup'),
]