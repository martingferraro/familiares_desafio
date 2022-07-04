from django.http import HttpResponse
from django.shortcuts import render
from familiapp.models import Padre
from familiapp.models import Madre

def padre(self):

    padre= Padre (nombre= "Martin",  fecha_nacimiento= "1948-11-15", años= "70")
    padre.save()
    texto= f"Familiar creado. Nombre: { padre.nombre }. Fecha de nacimiento: { padre.fecha_nacimiento } edad { padre.años }"
    return HttpResponse (texto)

def madre(self):

    madre= Madre (nombre= "María",  fecha_nacimiento= "1958-09-15", años= "65" )
    madre.save()
    texto= f"Familiar creado: Nombre: { madre.nombre }.  Fecha de nacimiento: { madre.fecha_nacimiento }, edad: { madre.años }"
    return HttpResponse (texto)