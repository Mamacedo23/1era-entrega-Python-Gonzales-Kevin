from django.http import HttpResponse
from django.shortcuts import render
from .models import Amores, Familia, Mascotas,Amores
from django.template import loader
from Coder.forms import MascotaFormulario,FamiliaFormulario,AmoresFormulario

# Create your views here.
def familiares(request):
    if request.method == "POST":
        miFormulario = FamiliaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            nombre = info.get("nombre")
            edad = info.get("edad")
            fec_nacimiento = info.get("fec_nacimiento")
            email = info.get("email")
            familiar = Familia(nombre=nombre,edad = edad, fec_nacimiento = fec_nacimiento, email = email)
            familiar.save()
            return render(request,"Coder/inicio.html",{"mensaje":"Familiar creado"})
        else:
            return render(request,"Coder/familiares.html",{"mensaje":"Familiar no creado"})
    else:
        miFormulario = FamiliaFormulario()
        return render(request,"Coder/familiares.html",{"formulario": miFormulario})

def mascotas(request):
    if request.method == "POST":
        miFormulario2 = MascotaFormulario(request.POST)
        print(miFormulario2)
        if miFormulario2.is_valid():
            nombre = request.POST.get("nombre")
            edad = request.POST.get("edad")
            raza = request.POST.get("raza")
            genero = request.POST.get("genero")
            estado = request.POST.get("estado")
            mascota = Mascotas(nombre=nombre,edad = edad, raza = raza, genero = genero, estado = estado)
            mascota.save()
            return render(request,"Coder/inicio.html",{"mensaje":"Mascota creado"})
        else:
            return render(request,"Coder/mascotas.html",{"mensaje":"Mascota no creado"})
    else:
        miFormulario2 = MascotaFormulario()
        return render(request,"Coder/mascotas.html",{"formulario2": miFormulario2})

def amores(request):
    if request.method == "POST":
        miFormulario3 = AmoresFormulario(request.POST)
        print(miFormulario3)
        if miFormulario3.is_valid():
            nombre = request.POST.get("nombre")
            edad = request.POST.get("edad")
            ocupacion = request.POST.get("ocupacion")
            tiempoRelacion = request.POST.get("tiempoRelacion")
            estadoRelacion = request.POST.get("estadoRelacion")
            amor = Amores(nombre=nombre,edad = edad, ocupacion = ocupacion, tiempoRelacion = tiempoRelacion, estadoRelacion = estadoRelacion)
            amor.save()
            return render(request,"Coder/inicio.html",{"mensaje":"Amor creado"})
        else:
            return render(request,"Coder/inicio.html",{"mensaje":"Amor no creado"})
    else:
        miFormulario3 = AmoresFormulario()
        return render(request,"Coder/amores.html",{"formulario3": miFormulario3})

def inicio(request):
    return render(request, "Coder/inicio.html")

def busquedaFamiliar(request):
    return render(request,"Coder/busquedaFamiliar.html")

def buscarFamiliar(request):
    if request.GET["edad"]:
        edad = request.GET.get("edad")
        familiares= Familia.objects.filter(edad=edad)
        if len(familiares) != 0:
            return render(request,"Coder/resultadoFamiliar.html",{"familiares": familiares})
        else:
            return render(request,"Coder/resultadoFamiliar.html",{"mensaje": "No hay familiar"})
    else:
        return render(request,"Coder/busquedaFamiliar.html",{"mensaje":"No enviaste datos"})
