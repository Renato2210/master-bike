# proyecto/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Arriendo
from .forms import ArriendoForm

def inicio(request):
    return redirect(reverse('catalogo'))

def formulario_arriendo(request):
    if request.method == 'POST':
        form = ArriendoForm(request.POST)
        if form.is_valid():
            arriendo = form.save(commit=False)
            arriendo.user = request.user
            arriendo.save()
            return redirect('recibo_arriendo', arriendo_id=arriendo.id)
    else:
        form = ArriendoForm()
    return render(request, 'app/formulario_arriendo.html', {'form': form})

def recibo_arriendo(request, arriendo_id):
    arriendo = get_object_or_404(Arriendo, id=arriendo_id)
    return render(request, 'app/recibo_arriendo.html', {'arriendo': arriendo})

def home(request):
    return render(request, 'app/PaginaP.html')

def crear_cuenta(request):
    return render(request, 'app/Crearcuenta.html')

def login(request):
    return render(request, 'app/login.html')

def olvidaste_contra(request):
    return render(request, 'app/olvidaste_contra.html')

def catalogo(request):
    return render(request, 'app/catalogo.html')

def arriendo(request):
    return render(request, 'app/arriendo.html')

def pagar_view(request):
    return render(request, 'app/pagar.html')
