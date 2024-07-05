from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='PaginaP'),
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('login/', views.login, name='login'),
    path('olvidaste_contra/', views.olvidaste_contra, name='olvidaste_contra'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('arriendo/', views.arriendo, name='arriendo'),
    path('formulario_arriendo/', views.formulario_arriendo, name='formulario_arriendo'),
    path('recibo_arriendo/<int:arriendo_id>/', views.recibo_arriendo, name='recibo_arriendo'),
    path('pagar/', views.pagar_view, name='pagar'),
]






