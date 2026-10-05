# path: función para definir una ruta individual
from django.urls import path

# views: importa las vistas de esta misma app
from . import views

# Lista de rutas de la app core
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
]