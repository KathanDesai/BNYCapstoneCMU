from django.conf.urls import url
from . import  views

urlpatterns = [
    #url(r'^login$', views.login, name='login'),
    url(r'^$', views.handle, name='homepage'),
    url(r'^ProcessRequest', views.BNYBackEndPost),
    url(r'^getModels', views.getModels)
    ]