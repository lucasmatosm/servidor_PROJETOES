from django.conf.urls import url
from povmt import views

urlpatterns = [
    url(r'^povmt/$', views.cria_usuario), #criar usuario
    url(r'^povmt/user/(?P<id_usuario>\d+)$', views.get_usuario), #recupera usuario pelo id
    url(r'^povmt/(?P<id_usuario>\d+)/$', views.criaAtividade), #atividades daquele usuario
    url(r'^povmt/atividade/(?P<id>\d+)/$', views.getAtividade), #pega uma atividade especifica
    url(r'^povmt/tilist/(?P<id_atividade>\d+)/$', views.criaTI), #lista e cria TI para um atividade
    url(r'^povmt/tiedit/(?P<id>\d+)/(?P<id_atividade>\d+)/$', views.editaTI), #edita um TI, no caso de aumentar horas
    url(r'^povmt/criatag/(?P<id_atividade>\d+)/$', views.criaTag), #cria tag para uma atividade
    url(r'^povmt/recuperaati/(?P<id>\d+)/$', views.recuperaAti),   #recupera atividade pelo id da tag associada
]
