from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    
    path('', views.procesar_pedido, name="procesar_pedido"),
]