from django.shortcuts import render, get_object_or_404
from .models import Proyecto, Tarea, Asignacion, Comentario, Etiqueta


def inicio(request):
    return render(request, 'index.html')

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()

    return render(request, 'proyectos.html', {
        'proyectos': proyectos
    })

def tareas_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    tareas = Tarea.objects.filter(
        proyecto=proyecto
    ).order_by('-fecha_creacion')

    return render(request, 'tareas_proyecto.html', {
        'proyecto': proyecto,
        'tareas': tareas
    })
    
def usuarios_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    asignaciones = Asignacion.objects.filter(
        tarea=tarea
    ).order_by('fecha_asignacion')

    return render(request, 'usuarios_tarea.html', {
        'tarea': tarea,
        'asignaciones': asignaciones
    }) 


def tareas_por_observacion(request, texto):
    asignaciones = Asignacion.objects.filter(
        observaciones__icontains=texto
    )

    tareas = Tarea.objects.filter(
        asignaciones__in=asignaciones
    ).distinct()

    return render(request, 'tareas_por_observacion.html', {
        'tareas': tareas,
        'texto': texto
    })
    

def tareas_completadas_por_anio(request, anio_inicio, anio_fin):
    tareas = Tarea.objects.filter(
        fecha_creacion__year__gte=anio_inicio,
        fecha_creacion__year__lte=anio_fin,
        estado="Completada"
    ).order_by('fecha_creacion')

    return render(request, 'tareas_completadas.html', {
        'tareas': tareas,
        'anio_inicio': anio_inicio,
        'anio_fin': anio_fin
    })


def ultimo_usuario_comentario(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    ultimo_comentario = Comentario.objects.filter(
        tarea__proyecto=proyecto
    ).order_by('-fecha_comentario').first()

    return render(request, 'ultimo_usuario_comentario.html', {
        'proyecto': proyecto,
        'ultimo_comentario': ultimo_comentario
    })


def comentarios_por_palabra_y_anio(request, tarea_id, palabra, anio):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    comentarios = Comentario.objects.filter(
        tarea=tarea,
        texto__istartswith=palabra,
        fecha_comentario__year=anio
    ).order_by('fecha_comentario')

    return render(request, 'comentarios_por_palabra_y_anio.html', {
        'tarea': tarea,
        'comentarios': comentarios,
        'palabra': palabra,
        'anio': anio
    })
    
def etiquetas_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    etiquetas = Etiqueta.objects.filter(
        tareas__proyecto=proyecto
    ).distinct().order_by('nombre')

    return render(request, 'etiquetas_proyecto.html', {
        'proyecto': proyecto,
        'etiquetas': etiquetas
    })
