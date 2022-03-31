from django.shortcuts import render
from .models import Proyecto #importar el modelo
# Create your views here.
def portfolio(request):
    proyectos = Proyecto.objects.all() #recupera todos los objetos de la clase
    #return render(request, "core/portfolio.html")
    #*****ruta actualizada al MVT que recibe un diccionario con los proyectos
    return render(request, "portfolio/portafolio.html",{'proyectos':proyectos}) #Inyecta los proyectos en página html
    #**************