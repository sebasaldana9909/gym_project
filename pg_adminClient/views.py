from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse

from pg_adminClient.forms import ClientForm
from pg_adminClient.models import Client
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views

# LoginRequiredMixin deben ir en todas las vistas que se vayan a crear


class pg_AdminClient(LoginRequiredMixin, generic.ListView):
    model = Client
    template_name = 'pg_adminClient/pg_adminClient.html'
    content_object_name = "clients"
    login_url = "/login/"

class InsertClient(LoginRequiredMixin, generic.CreateView):
    model = Client
    template_name = 'pg_adminClient/form.html'
    context_object_name = "clients"
    form_class = ClientForm
    success_url = reverse_lazy("pg_adminClient:client_list")
    login_url = "/login/"

class BorrarClient(LoginRequiredMixin, generic.DeleteView):
    model = Client
    template_name = 'pg_adminClient/delete.html'
    context_object_name = "clients"
    form_class = ClientForm
    success_url = reverse_lazy("pg_adminClient:client_list")
    login_url = "/login/"

#Añadir class Editar
