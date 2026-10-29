from django.db import models


class Compania(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_hora_anadida = models.DateTimeField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return self.nombre