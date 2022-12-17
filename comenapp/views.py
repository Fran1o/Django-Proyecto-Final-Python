from django.shortcuts import render, redirect
from django.dispatch import receiver
from comenapp.models import *
from comenapp.forms import *
from django.contrib.auth.models import User

# CVB

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

# Django authentication

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def mostrar_comen(request):

    comen = Coment.objects.all()

    return render(request, "comenapp/comen_list.html", {"list_comentarios":comen})

def form_comen(request):
    usuario = User.objects.all()
    if request.method == "POST":
        fcomen = ComentForm(request.POST)
        
        if fcomen.is_valid():
            data = fcomen.cleaned_data
            usuario = User()
            usuario.username = request.POST.get('nombre')
            comentario = Coment(Remitente=usuario["Remitente"], Contenido=data["Contenido"])
            comentario.save()
    fcomen = ComentForm()

    return render(request, "comenapp/comen_create.html", {"form_comentarios":fcomen})