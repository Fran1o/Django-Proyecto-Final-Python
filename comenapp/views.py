from django.shortcuts import render, redirect
from comenapp.models import *
from comenapp.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def form_comen(request):
    comen = Coments.objects.all()

    usuario = request.user

    if request.method == "POST":

        fcomen = ComentForm(request.POST)

        if fcomen.is_valid():

            coment = fcomen.save(commit=False)
            coment.remitente = request.user 
            coment.save()
            
        return redirect("lcomen")

    else:

        fcomen = ComentForm()
        
    return render(request, "comenapp/comen_list.html", {"form_comentarios": fcomen, "list_comentarios":comen, "usuarios": usuario})


@login_required
def eliminar_comentario(request, id):
    

    comentario = Coments.objects.get(id=id)
    comentario.delete()

    return redirect("lcomen")



