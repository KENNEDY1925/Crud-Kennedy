from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro  
from .forms import Libroform

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def Libros(request):
    libros = Libro.objects.all()  # Cambié el nombre a minúsculas por convención
    return render(request, 'libros/index.html', {'Libros': libros})

def crear(request):
    formulario = Libroform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')  # Redirige a la lista de libros

    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libro = get_object_or_404(Libro, id=id)  
    formulario = Libroform(request.POST or None, request.FILES or None, instance=libro)

    if formulario.is_valid():
        formulario.save()
        return redirect('libros')

    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = get_object_or_404(Libro, id=id)  
    libro.delete()
    return redirect('libros')
