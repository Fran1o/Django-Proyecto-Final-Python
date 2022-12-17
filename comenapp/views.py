from django.shortcuts import render
from comenapp.models import *
from comenapp.forms import *


# Create your views here.

def form_comen(request):
    comen = Coment.objects.all()
    if request.method == "POST":

        fcomen = ComentForm(request.POST)
        comen = Coment.objects.all()
        if fcomen.is_valid():
                
            data = fcomen.cleaned_data
            comentario = Coment(remitente=data["remitente"], contenido=data["contenido"], fecha=data["fecha"])
            comentario.save()

        return render(request, "comenapp/comen_list.html")
            
    else:

        fcomen = ComentForm()

    return render(request, "comenapp/comen_list.html", {"form_comentarios": fcomen, "list_comentarios": comen})

