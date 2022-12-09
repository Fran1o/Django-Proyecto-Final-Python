from django.urls import path
from blogapp.views import *
from blogapp.sesionViews import *

urlpatterns = [
    path('home/', mostrar_articulos, name="home"),
    path('creararticulo/', crear_articulo),
    path('articulo/<id>', mostrar_articulo_completo, name="mostrar-articulo"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup")
]