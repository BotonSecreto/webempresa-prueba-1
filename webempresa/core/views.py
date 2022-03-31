from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"core/home.html")  #método render invoca al template
 
def about(request):
    return render(request,"core/about.html")  #método render invoca al template

def services(request):
    return render(request,"core/services.html")  #método render invoca al template

def store(request):
    return render(request,"core/store.html")  #método render invoca al template
