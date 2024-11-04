from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listaE'),
    path('listadoDeEditoriales/', views.listaEditoriales, name='listaE'),
    path('editoriales/<int:id_editorial>/', views.detalleEDITORIAL, name="detalle"),
]
