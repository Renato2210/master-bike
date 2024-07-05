"""
URL configuration for proyectobike project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from proyecto import views

urlpatterns = [
    path('', views.home, name='PaginaP'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('login/', views.login, name='login'),
    path('crearcuenta/', views.crear_cuenta, name='Crearcuenta'),
    path('olvidaste_contra/', views.olvidaste_contra, name='olvidaste_contra'),
    path('arriendo/', views.arriendo, name='arriendo'),
    path('pagar/', views.pagar_view, name='pagar'),  
    path('formulario_arriendo/', views.formulario_arriendo, name='formularioarriendo'),
    path('recibo_arriendo/<int:arriendo_id>/', views.recibo_arriendo, name='recibo_arriendo'),
]

