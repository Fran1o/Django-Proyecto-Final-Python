from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from blogapp.forms import UsuarioRegisterFormulario

def login(request):
    
    #Agregar {{request.user}} en la pagina principal para verificar que este logeado el usuario trayendo el nombre de usuario

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            user = authenticate(username = data["username"], password=data["password"])

            if user is not None:
                login(request,user)
                return redirect("home")

            else:
                return render(request, "blogapp/sesion/login.html", {"form": formulario, "erorrs": "Credenciales incorrectas"})

        else:
            return render(request, "blogapp/sesion/login.html", {"form": formulario, "erorrs": formulario.errors})
    

    formulario = AuthenticationForm()
    return render(request, "blogapp/sesion/login.html", {"form": formulario, "errors": errors})



def signup(request):

    #Modificar esto para usar un "Model Form"

    if request.method == "POST":
        formulario = UsuarioRegisterFormulario(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
        
        else:
            return render(request, "blogapp/sesion/signup.html", {"form": formulario, "errors":formulario.errors})


    formulario = UsuarioRegisterFormulario()
    return render(request, "blogapp/sesion/signup.html", {"form": formulario})