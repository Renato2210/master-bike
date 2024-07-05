# proyecto/views.py

from django.shortcuts import render, redirect
from .forms import PagoForm

def home(request):
    return render(request, 'app/PaginaP.html')

def catalogo(request):
    return render(request, 'app/catalogo.html')

def login(request):
    return render(request, 'app/login.html')

def crear_cuenta(request):
    return render(request, 'app/Crearcuenta.html')

def olvidaste_contra(request):
    return render(request, 'app/olvidastecontra.html')

def arriendo(request):
    return render(request, 'app/arriendo.html')

def pagar_view(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PaginaP')  # Redirigir a una página de confirmación o principal
    else:
        form = PagoForm()
    
    return render(request, 'app/pagar.html', {'form': form})
