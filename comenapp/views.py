from django.shortcuts import render
from django.dispatch import receiver
from message.models import *
from message.forms import *

# CVB

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

# Django authentication

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
