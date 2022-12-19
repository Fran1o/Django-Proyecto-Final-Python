from django.urls import path , include
from blogapp.views import *
from blogapp.sesionViews import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('home/', mostrar_articulos, name="home"),
    path('creararticulo/<id>', crear_articulo, name="crear"),
    path('mascota/<id>', mostrar_articulo_completo, name="mostrar-mascota"),
    
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", LogoutView.as_view(template_name="blogapp/logout.html"), name="logout"),

    path("perfil/<id>", perfil_user, name="perfil"),
    path("addfoto/<id>", agregar_foto, name="agregar-foto"),
    path("editarfoto/<id>", editar_foto, name="editar-foto"),
    path("perfileditav/<id>", editar_username, name="editar-username"),

    path("contacto/", contacto, name="contacto"),

    path("adoptar/<id>", funcion_adoptar, name="adoptar"),

    path("adopt/", adopt, name="adopt"),

    path("comentarios/", include('comenapp.urls')),
]


