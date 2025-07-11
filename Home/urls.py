from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    path('agregar-autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar-editorial/', views.agregar_editorial, name='agregar_editorial'),
    path('buscar-libro/', views.buscar_libro, name='buscar_libro'),
]