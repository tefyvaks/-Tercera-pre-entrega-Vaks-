from django.shortcuts import render
from django.http import HttpResponse
from BibliotecaApp.models import Libro, Socio, Editorial
from BibliotecaApp.forms import LibroFormulario
# Create your views here.

def inicio(request):
    return render(request, "BibliotecaApp/inicio.html")

def editorial(request):
    return render(request, "BibliotecaApp/editorial.html")

def libros(request):
    return render(request, "BibliotecaApp/libros.html")

def socios(request):
    return render(request, "BibliotecaApp/socios.html")

def libroFormulario(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        genero = request.POST.get('genero')

        nuevo_libro = Libro(titulo=titulo, autor=autor, genero=genero)
        nuevo_libro.save()

        return render(request, "BibliotecaApp/inicio.html")

    return render(request, "BibliotecaApp/libroFormulario.html")

def libroBusqueda (request):
    return render(request, "BibliotecaApp/libroBusqueda.html")

def resultados(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        libros = Libro.objects.filter(titulo__icontains=titulo)
        return render(request, "BibliotecaApp/resultados.html", {'libros': libros, 'titulo': titulo})

    else:
        respuesta = "No enviaste datos."


    return HttpResponse(respuesta)


