from django.db import models

class UsuarioMobike(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    edad = models.IntegerField()
    email = models.EmailField(max_length=255)
    direccion = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombres + " " + self.apellidos









