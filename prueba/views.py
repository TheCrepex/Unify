from django.http import HttpResponse
from django.shortcuts import render

def Saludo(request):
    return HttpResponse("Hola Mundo")

def Despedida(request):
    return HttpResponse("Adios")

def Adulto(request,edad):
    if int(edad) >= 18:
        return HttpResponse("Es adulto")
    else:
        return HttpResponse("No es adulto")

def Simple(request):
    return render(request,'Simple.html',{})

def Dinamico(request,name):
    categories = ['code', 'desing', 'marketing', 'business']
    context = {'name' : name, 'categories':categories}
    
    return render(request, 'Dinamico.html', context)

def Estaticos(request):
    return render(request,'Estaticos.html',{})