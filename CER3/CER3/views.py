from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    title = "Inicio"

    data = {
        "title": title,
    }

    return render(request,'CER3/index.html', data)

def carreras(request):
    title = "Carreras"
    total_carreras = 3
    data = {
        "title": title,
        "total_carreras":total_carreras
    }
    return render(request,'dummydata',data)

def docentes(request):
    title = "Docentes"
    
    data = {
        "title": title,
    }
    return render(request,'dummydata',data)