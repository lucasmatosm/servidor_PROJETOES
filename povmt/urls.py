from django.conf.urls import url
from povmt import views

urlpatterns = [
    url(r'^povmt/$', views.cria_usuario),
    url(r'^povmt/(?P<id_usuario>\d+)/$', views.criati),



]