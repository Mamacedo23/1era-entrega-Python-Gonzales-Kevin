from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fec_nacimiento = models.DateField()
    email = models.EmailField()
    def __str__(self):
        return self.nombre + "" + str(self.edad) + "" + str(self.fec_nacimiento) + self.email

class Mascotas(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    raza = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    estado = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre + "" + str(self.edad) + "" + self.raza + self.genero + self.estado

class Amores(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    ocupacion = models.CharField(max_length=30)
    tiempoRelacion = models.CharField(max_length=30)
    estadoRelacion = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre + "" + str(self.edad) + "" + self.ocupacion + self.tiempoRelacion + self.estadoRelacion