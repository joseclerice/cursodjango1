from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "global/home.html")


def sobre(request):
    return HttpResponse("Sobre Nós")


def contato(request):
    return HttpResponse("Contate-nos")
