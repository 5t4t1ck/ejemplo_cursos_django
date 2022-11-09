from django.shortcuts import render
#from django.http import HttpResponse
from .models import Curso

def homepage(request):
    #return HttpResponse("Hola esto es Django desde la App")
    return render(request, "main/inicio.html",{"cursos":Curso.objects.all})