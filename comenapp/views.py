from django.shortcuts import render, redirect
from comenapp.models import *
from comenapp.forms import *


# Create your views here.

def mostrar_comen(request):

    comen = Coment.objects.all()

    return render(request, "comenapp/comen_list.html", {"list_comentarios": comen})

def form_comen(request):

    if request.method == "POST":

        fcomen = ComentForm(request.POST)
        
        if fcomen.is_valid():

            data = fcomen.cleaned_data
            comentario = Coment(remitente=data["remitente"], contenido=data["contenido"], fecha=data["fecha"])
            comentario.save()

        return render(request, "comenapp/comen_list.html")
            
    else:

        fcomen = ComentForm()

    return render(request, "comenapp/comen_create.html", {"form_comentarios": fcomen})

