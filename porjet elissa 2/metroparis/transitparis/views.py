from django.shortcuts import render, redirect #a changer
from django.http import HttpResponse
from .models import transport
import random
from django.shortcuts import render

def index(request):
    return render(request, "transitparis/index.html", {"all_wagon": transport.objects.all(), "random": random.randint(1, 20)})

def show(request, id_paris):
    mes_metro = transport.objects.get(id=id_paris)
    return render(request, "transitparis/show.html", {
        "id": mes_metro.id,
        "debut": mes_metro.debut,
        "fin": mes_metro.fin,
        "imgligne": mes_metro.imgligne,
        "nextID": int(id_paris) + 1,
    })
