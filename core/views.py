# render: función que combina una plantilla con datos y arma la respuesta HTTP
from django.shortcuts import render

# connection: objeto de Django que expone la configuración de la base de datos activa
from django.db import connection


# def: toda vista es una función que recibe "request" (la petición del navegador)
def inicio(request):
    # settings_dict: diccionario interno con ENGINE, HOST, NAME, etc. de la conexión activa
    info_bd = connection.settings_dict

    # contexto: los datos que la plantilla va a poder usar con {{ variable }}
    contexto = {
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }

    # render: junta el template "core/inicio.html" con el contexto y devuelve el HTML final
    return render(request, 'core/inicio.html', contexto)


def servicios(request):
    servicios = [
        {'nombre': 'Desarrollo Web', 'descripcion': 'Creación de aplicaciones web modernas.'},
        {'nombre': 'Bases de Datos', 'descripcion': 'Diseño y administración de bases de datos.'},
        {'nombre': 'Aplicaciones Móviles', 'descripcion': 'Desarrollo de aplicaciones para dispositivos móviles.'},
    ]

    contexto = {
        'servicios': servicios
    }

    return render(request, 'core/servicios.html', contexto)


# Vista de contacto
def contacto(request):
    return render(request, 'core/contacto.html')