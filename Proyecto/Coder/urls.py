from django.urls import path 
from Coder import views

urlpatterns = [
    path('',views.inicio, name = 'inicio'),
    path('familiares/',views.familiares,name="familiares"),
    path('mascotas/',views.mascotas,name="mascotas"),
    path('amores/',views.amores, name = "amores"),
    path('busquedaFamiliar/',views.busquedaFamiliar, name = "busquedaFamiliar"),
    path('buscarFamiliar/',views.buscarFamiliar, name = "buscarFamiliar"),
]
