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

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    compania = models.ForeignKey(
        Compania,
        on_delete=models.CASCADE,
        related_name="proyectos"
    )

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    ESTADOS = [
        ("Pendiente", "Pendiente"),
        ("En progreso", "En progreso"),
        ("Completada", "Completada"),
    ]

    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name="tareas"
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)

    usuarios = models.ManyToManyField(
        Usuario,
        through="Asignacion",
        related_name="tareas"
    )

    etiquetas = models.ManyToManyField(
        "Etiqueta",
        related_name="tareas",
        blank=True
    )

    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE,
        related_name="asignaciones"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="asignaciones"
    )
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ["fecha_asignacion"]
        constraints = [
            models.UniqueConstraint(
                fields=["tarea", "usuario"],
                name="asignacion_unica_por_tarea_usuario"
            )
        ]

    def __str__(self):
        return f"{self.usuario} - {self.tarea}"


class Comentario(models.Model):
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_comentario"]

    def __str__(self):
        return f"Comentario de {self.usuario} en {self.tarea}"


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre