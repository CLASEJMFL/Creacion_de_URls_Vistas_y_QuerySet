from django.shortcuts import render, get_object_or_404
from .models import Proyecto, Tarea, Asignacion


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