# En views.py
from django.shortcuts import render, redirect
from .forms import ImagenForm
from .models import Imagen

def subir_imagen(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ver_imagenes')
    else:
        form = ImagenForm()
    return render(request, 'subir_imagen.html', {'form': form})

def ver_imagenes(request):
    imagenes = Imagen.objects.all()
    return render(request, 'ver_imagenes.html', {'imagenes': imagenes})
