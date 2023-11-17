from django.urls import path
from . import views
from .views import ProyectoLibros, FormLibro, Detalles


urlpatterns = [
    path('', ProyectoLibros.as_view(), name='listadoLibros'),
    path('Formlibros', FormLibro.as_view(), name='FormLibro'),
    path('detalles/<int:pk>/', Detalles.as_view(), name='detalles'),
]