from django.http import HttpResponse 
from django.template import Template,Context


def saluda(request):
    return HttpResponse("Hola como va? Bienvenido")


def prueba_template(request):
    mi_html=open("C:/Users/Gonzalo/OneDrive/Desktop/Gonza Staffs/Python/git_djangoprueba2/djangoprueba2/Proyecto1gonza/Proyecto1gonza/index.html")
    plantilla=Template(mi_html.read())
    mi_html.close()
    contexto=Context(
     {
         "my_name":"Gonzalo",
         "my_apellido":"Herrero" 
         
     }   
        
    )
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
     