from socket import fromshare
from django import forms 

class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    raza = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    estado = forms.CharField(max_length=30)

class FamiliaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fec_nacimiento = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)

class AmoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    ocupacion = forms.CharField(max_length=30)
    tiempoRelacion = forms.CharField(max_length=30)
    estadoRelacion = forms.CharField(max_length=30)