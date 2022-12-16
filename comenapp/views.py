from django.shortcuts import render, redirect
from django.dispatch import receiver
from comenapp.models import *
from comenapp.forms import *


# CVB

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

# Django authentication

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MessagesList(LoginRequiredMixin, ListView):

    model = Coment
    template_name = "comentarios/Coment_list.html"

class MessageDetail(LoginRequiredMixin, DetailView):

    model = Coment
    template_name = "comentarios/Coment_detail.html"

class MessageCreate(LoginRequiredMixin, CreateView):

    model = Coment
    success_url = "project/comentarios"
    fields = ['Titulo','Remitente', 'Destinatario', 'Contenido', 'Fecha']
# def MessageCreate(request):

#     if request.method == "POST":
#         comform = ComentForm(request.POST)

#         if comform.is_valid():

#             data = comform.cleaned_data
#             mascotas = Coment(Titulo=data["Titulo"], Remitente=data["Remitente"], Destinatario=data["Destinatario"], Contenido=data["Contenido"], Fecha=data["Fecha"])
#             mascotas.save()

#         return redirect("home")

#     else:

#         comform = ComentForm()

#     return render(request, "comenapp/Coment_form.html", {"comform": comform})
   
    

class MessageDelete(LoginRequiredMixin, DeleteView):

    model = Coment
    success_url = "/comentarios/"