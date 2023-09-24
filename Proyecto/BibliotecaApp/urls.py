from django.urls import path
from BibliotecaApp import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('editorial/', views.editorial, name="Editorial"),
    path('libros/', views.libros, name="Libros"),
    path('socios/', views.socios, name="Socios"),
    path('libroFormulario/', views.libroFormulario, name="Formulario Libro"),
    path('libroBusqueda/', views.libroBusqueda, name="Busqueda Libro"),
    path('resultados/', views.resultados, name="Resultados"),
]
