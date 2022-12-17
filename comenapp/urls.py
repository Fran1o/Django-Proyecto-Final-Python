from django.urls import path
from comenapp.views import *

urlpatterns = [
    path('lcomen/', form_comen, name="lcomen"),
]