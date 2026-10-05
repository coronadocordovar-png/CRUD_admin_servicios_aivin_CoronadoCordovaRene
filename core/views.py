from django.shortcuts import render
from django.db import connection
from .models import Servicio


def inicio(request):
    info_bd = connection.settings_dict

    contexto = {
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }

    return render(request, 'core/inicio.html', contexto)


def servicios(request):
    servicios = Servicio.objects.all()

    contexto = {
        'servicios': servicios
    }

    return render(request, 'core/servicios.html', contexto)


def contacto(request):
    return render(request, 'core/contacto.html')
