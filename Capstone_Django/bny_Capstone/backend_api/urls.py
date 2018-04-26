from django.conf.urls import url
from . import  views

urlpatterns = [
    #url(r'^login$', views.login, name='login'),
    url(r'^$', views.handle, name='homepage'),
    url(r'^ProcessRequest', views.BNYBackEndPost),
<<<<<<< HEAD
    url(r'^getData', views.getData),
=======
    url(r'^getModels', views.getModels),
    url(r'^getOverlaps', views.getOverlaps)
>>>>>>> 3e5edaf6947aaa5d130a05bcea820e9279aa6779
    ]