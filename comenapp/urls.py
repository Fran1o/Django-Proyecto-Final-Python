from django.urls import path
from comenapp.views import *

urlpatterns = [
    path('lcomen/', mostrar_comen, name="lcomen"),
    path('fcomen/', form_comen, name="fcomen"),
]