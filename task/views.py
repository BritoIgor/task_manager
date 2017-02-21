from django.shortcuts import render
from django.http import HttpResponse

class Tarefa(object):
    def __init__(self, titulo, data):
        self.titulo = titulo
        self.data = data
    def __Str__(Self):
        return self.titulo


def home(request):
    return HttpResponse("Home(r)!")

def sobre(request):
    return HttpResponse("Igor")

def tarefa(request, num):
    return HttpResponse("Tarefa: "+str(num))

def tarefa(request, ano, mes, dia):
    return HttpResponse("Data: "+str(ano))
