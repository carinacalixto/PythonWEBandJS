from django.http import HttpResponse
from django.shortcuts import HttpResponse, render

# Create your views here.

# def index (request):
#     return HttpResponse("Hello!")
def index(request):
    return render(request, "hello/index.html")

def carina(request):
    return HttpResponse("Hello, Carina!")

def david(request):
    return HttpResponse("Hello, David!")

def brian(request):
    return HttpResponse("Hello, Brian!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name" : name.capitalize()
    })