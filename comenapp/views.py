from django.shortcuts import render
from comenapp.models import *
from comenapp.forms import *


# Create your views here.

def form_comen(request):
    comen = Coments.objects.all()
    if request.method == "POST":

        fcomen = ComentForm(request.POST)
        comen = Coments.objects.all()
        if fcomen.is_valid():
                
            data = fcomen.cleaned_data
            comentario = Coments(remitente=data["remitente"], contenido=data["contenido"], fecha=data["fecha"])
            comentario.save()

        return render(request, "comenapp/comen_list.html")
            
    else:

        fcomen = ComentForm()

    return render(request, "comenapp/comen_list.html", {"form_comentarios": fcomen, "list_comentarios": comen})

