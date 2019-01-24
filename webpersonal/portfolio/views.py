from django.shortcuts import render
from .models import project

# Create your views here.    //"python.pythonPath": "C:\\Users\\gabmc\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe",


def porfolio(request):
    projectos= project.objects.all() #proyectos creados en portfolio a travez del menu admin

    return render(request,"portfolio/portfolio.html",{'projects': projectos})
