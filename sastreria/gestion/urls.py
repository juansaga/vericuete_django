from django.urls import path
from .views import lista_clientes, home

urlpatterns = [
    path('clientes/', lista_clientes, name='lista-clientes'),
    path('', home, name='home'),
]
