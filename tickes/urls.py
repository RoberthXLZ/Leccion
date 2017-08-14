from django.conf.urls import include, url

from tickes.views import create, index_ticket, eliminarTicket,editarTicket

urlpatterns = [
    url(r'^$',index_ticket, name = 'index'),
    url(r'^createRecibo$',createRecibo, name = 'createTicket'),
    url(r'^create$',create, name = 'create'),
    url(r'^editar/(?P<id>\d+)$',editarTicket, name='editarTicket'),
    url(r'^eliminar/(?P<id>\d+)$',eliminarTicket, name='eliminarTicket'),
]