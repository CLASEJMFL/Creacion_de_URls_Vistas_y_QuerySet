from django.contrib import admin
from .models import Compania, Administrador, Usuario

admin.site.register(Compania)
admin.site.register(Administrador)
admin.site.register(Usuario)