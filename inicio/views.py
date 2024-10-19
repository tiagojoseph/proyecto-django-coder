from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render

def mi_vista (request):
    return HttpResponse ("soy la vista")

def inicio (request):
    return HttpResponse ("soy la pantalla de inicio")

def vista_datos1 (request, nombre):
    nombre_mayuscula = nombre.upper()
    return HttpResponse (f"hola {nombre_mayuscula}")

def primer_template (request):
    #sin with 
    archivo_del_template = open(r"templates\primer_template.html")
    template = Template (archivo_del_template.read())
    archivo_del_template.close() 
    contexto = Context()  

    render_template = template.render(contexto)

    return HttpResponse (render_template)

def segundo_template (request):
    
    fecha_actual = datetime.now()
    datos = {"fecha_actual" : fecha_actual,
             "numeros": list(range(1,11))}

    #v1
    #archivo_del_template = open(r"templates\segundo_template.html")
    #template = Template (archivo_del_template.read())
    #archivo_del_template.close() 


    #contexto = Context(datos)  

    #render_template = template.render(contexto)

    #v2 

    #template = loader.get_template("segundo_template.html")

    #render_template = template.render(datos)

    #return HttpResponse (render_template)

    #v3
    
    return render (request, "segundo_template.html", datos)