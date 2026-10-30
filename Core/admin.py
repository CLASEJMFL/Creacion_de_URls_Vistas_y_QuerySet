from django.contrib import admin
from .models import (
    Compania,
    Administrador,
    Usuario,
    Proyecto,
    Tarea,
    Asignacion,
    Comentario,
    Etiqueta,
)

admin.site.register(Compania)
admin.site.register(Administrador)
admin.site.register(Usuario)
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Asignacion)
admin.site.register(Comentario)
admin.site.register(Etiqueta)