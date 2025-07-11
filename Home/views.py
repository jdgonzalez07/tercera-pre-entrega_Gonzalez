# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     return render(request,'index.html')

from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm, AutorForm, EditorialForm

def inicio(request):
    return render(request, "inicio.html")

def agregar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = LibroForm()
    return render(request, "libro_form.html", {"form": form})

def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = AutorForm()
    return render(request, "autor_form.html", {"form": form})

def agregar_editorial(request):
    if request.method == "POST":
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = EditorialForm()
    return render(request, "editorial_form.html", {"form": form})

def buscar_libro(request):
    libros = []
    if "titulo" in request.GET:
        titulo = request.GET["titulo"]
        libros = Libro.objects.filter(titulo__icontains=titulo)
    return render(request, "buscar_libro.html", {"libros": libros})