from django.shortcuts import render, redirect
from blogapp.models import Mascotas, Contacto, Adoptar, User, Avatar
from blogapp.forms import MascotaFormulario, ContactoFormulario, AdoptarFormulario, AvatarForm, UserEditForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#Form para crear mascotas

def crear_articulo(request, id):

    usuarios = User.objects.get(id=id)

    if request.method == "POST":
        formulario = MascotaFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            mascotas = Mascotas(nombre=data["nombre"], animal=data["animal"], raza=data["raza"], edad=data["edad"], color=data["color"], imagen=data["imagen"] )
            mascotas.save()

        return redirect("home")

    else:

        formulario = MascotaFormulario()

    return render(request, "blogapp/crear_articulo_form.html", {"formulario": formulario, "usuarios": usuarios})

#Mostrando mascotas

def mostrar_articulos(request):

    mascotas = Mascotas.objects.all()

    if request.method == "POST":

        formulario = MascotaFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            mascotas = Mascotas()
            mascotas.nombre = request.POST.get('nombre')
            mascotas.animal = request.POST.get('animal')
            mascotas.raza = request.POST.get('raza')
            mascotas.edad = request.POST.get('edad')
            mascotas.color = request.POST.get('color')
            mascotas.imagen = request.FILES.get('imagen')
            mascotas.save()

        return render(request, "blogapp/index.html", {"mascotas": mascotas})

    else:

        return render(request, "blogapp/mostrar_articulos.html", {"mascotas": mascotas})

#Views para mostrar info mascotas

def mostrar_articulo_completo(request, id):

    mascotas = Mascotas.objects.get(id=id)

    return render(request, "blogapp/mostrar_articulo_completo.html", {"mascotas": mascotas})

#Form contacto

def contacto(request):

    if request.method == "POST":
        formulario = ContactoFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            infocontacto = Contacto(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], asunto=data["asunto"], mensaje=data["mensaje"])
            infocontacto.save()

        return redirect("home")

    else:

        formulario = ContactoFormulario()

    return render(request, "blogapp/contacto.html", {"formulario": formulario})

#Form adoptar mascota

def funcion_adoptar(request, id):

    mascotas = Mascotas.objects.get(id=id)

    if request.method == "POST":
        formulario = AdoptarFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            infoadoptante = Adoptar(nombre=data["nombre"], apellido=data["apellido"], celular=data["celular"], direccion=data["direccion"])
            infoadoptante.save()

        return redirect("adopt")

    else:

        formulario = AdoptarFormulario()

    return render(request, "blogapp/form_adoptar.html", {"formulario": formulario, "mascotas": mascotas})


def adopt(request):

    return render(request, "blogapp/adopt.html") 


#Perfil del usuario
@login_required

def perfil_user(request, id):

    usuarios = User.objects.get(id=id)

    if request.user.is_authenticated:

        imagen_model = Avatar.objects.filter(user=request.user.id).order_by("-id")

        if len(imagen_model) > 0:

            imagen_url = imagen_model[0].img.url

            return render(request, "blogapp/perfil.html", {"usuarios": usuarios, "imagen_url": imagen_url})

        else:

            imagen_url = ""

    else:
        imagen_url = ""
    
    return render(request, "blogapp/perfil.html", {"usuarios": usuarios, "imagen_url": imagen_url})


#Agregar foto

def agregar_foto(request, id):

    usuarios = User.objects.get(id=id)

    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")

        if formulario.is_valid():

            data = formulario.cleaned_data
            usuario = request.user

            avatar = Avatar(user=usuario, img=data['img'])
            avatar.save()

            if len(imagen_model) > 0:

                imagen_url = imagen_model[0].img.url

                return redirect("home")
            else:

                imagen_url = ""

                return render(request, "blogapp/agregar_foto.html", {"formulario": formulario, "usuarios": usuarios, "imagen_url": imagen_url})

        else:

            imagen_url = ""

            return render(request, "blogapp/agregar_foto.html", {"formulario": formulario, "usuarios": usuarios, "imagen_url": imagen_url})

    else:

        formulario = AvatarForm()

    return render(request, "blogapp/agregar_foto.html", {"formulario": formulario, "usuarios": usuarios})


#Editar username

def editar_username(request, id):

    usuarios = User.objects.get(id=id)

    usuario = request.user

    imagen_model = Avatar.objects.filter(user=request.user.id).order_by("-id")
    
    if request.method == "POST":

        formulario = UserEditForm(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            usuario.username = data["username"]
            usuario.save()

            return redirect("home")

    else:

        if len(imagen_model) > 0:

            formulario = UserEditForm()

            imagen_url = imagen_model[0].img.url

            return render(request, "blogapp/editar_username.html", {"usuarios": usuarios, "imagen_url": imagen_url, "formulario": formulario})

        else:

            formulario = UserEditForm()

            imagen_url = ""

            return render(request, "blogapp/editar_username.html", {"usuarios": usuarios, "imagen_url": imagen_url, "formulario": formulario})

    
    formulario = UserEditForm()


    return render(request, "blogapp/editar_username.html", {"usuarios": usuarios, "imagen_url": imagen_url, "formulario": formulario})


#Editar foto

def editar_foto(request, id):

    usuarios = User.objects.get(id=id)

    imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")

    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            usuario = request.user

            avatar = Avatar(user=usuario, img=data['img'])
            avatar.save()

            imagen_url = imagen_model[0].img.url

        return render(request, "blogapp/editar_foto.html", {"formulario": formulario, "usuarios": usuarios, "imagen_url": imagen_url})

    else:

        imagen_url = imagen_model[0].img.url

        formulario = AvatarForm()

    return render(request, "blogapp/editar_foto.html", {"formulario": formulario, "usuarios": usuarios, "imagen_url": imagen_url})
