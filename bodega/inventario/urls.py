from django.urls import path
from . import views
from .views import lista_productos, agregar_producto, editar_producto, eliminar_producto, buscar_productos  # Importar la vista desde views.py
urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
