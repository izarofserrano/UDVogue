from django.shortcuts import render
from .models import Editorial

# Create your views here.

def listaEditoriales(request):
    editoriales = Editorial.objects.order_by('nombre')
    nombre_editoriales = ', '.join([editoriales.nombre for editorial in editoriales])
    return HttpResponse(nombre_editoriales)