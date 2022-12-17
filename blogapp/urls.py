from django.urls import path
from blogapp.views import *
from blogapp.sesionViews import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', mostrar_articulos, name="home"),
    path('creararticulo/', crear_articulo),
    path('mascota/<id>', mostrar_articulo_completo, name="mostrar-mascota"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("contacto/", contacto, name="contacto"),
    path("adoptar/<id>", funcion_adoptar, name="adoptar"),
    path("adopt/", adopt, name="adopt"),
    path("logout/", LogoutView.as_view(template_name="blogapp/logout.html"), name="logout"),
]


