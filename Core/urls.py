"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path
from Proyecto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('proyectos/', views.lista_proyectos, name='proyectos'),

    # Ejercicio 3
    path(
        'proyectos/<int:proyecto_id>/tareas/',
        views.tareas_proyecto,
        name='tareas_proyecto'
    ),

    # Ejercicio 4
    path(
        'tareas/<int:tarea_id>/usuarios/',
        views.usuarios_tarea,
        name='usuarios_tarea'
    ),
    
    # Ejercicio5
    path(
    'tareas/observaciones/<str:texto>/',
    views.tareas_por_observacion,
    name='tareas_por_observacion'
    ),
    
    # Ejercicio 6
    path(
        'tareas/completadas/<int:anio_inicio>/<int:anio_fin>/',
        views.tareas_completadas_por_anio,
        name='tareas_completadas_por_anio'
    ),
    
    # Ejercicio 7
    path(
        'proyectos/<int:proyecto_id>/ultimo-comentario/',
        views.ultimo_usuario_comentario,
        name='ultimo_usuario_comentario'
    ),
    
    # Ejercicio 8
    path(
        'tareas/<int:tarea_id>/comentarios/<str:palabra>/<int:anio>/',
        views.comentarios_por_palabra_y_anio,
        name='comentarios_por_palabra_y_anio'
    ),
    
    # Ejercciio 9
    path(
        'proyectos/<int:proyecto_id>/etiquetas/',
        views.etiquetas_proyecto,
        name='etiquetas_proyecto'
    ),

    #Ejercicio 10
    path(
        'usuarios/sin-tareas/',
        views.usuarios_sin_tareas,
        name='usuarios_sin_tareas'
    ),
]
#Ejercicio 11
handler400 = 'Proyecto.views.error_400'
handler403 = 'Proyecto.views.error_403'
handler404 = 'Proyecto.views.error_404'
handler500 = 'Proyecto.views.error_500'




