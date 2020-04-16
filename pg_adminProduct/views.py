from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from pg_adminProduct.models import Product
from pg_adminProduct.forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views

# LoginRequiredMixin deben ir en todas las vistas que se vayan a crear

class pg_AdminProduct(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = 'pg_adminProduct/pg_adminProduct.html'
    content_object_name = "products"
    login_url = "/login/"

class InsertProduct(LoginRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'pg_adminProduct/form.html'
    context_object_name = "products"
    form_class = ProductForm
    success_url = reverse_lazy("pg_adminProduct:product_list")
    login_url = "/login/"

class BorrarProduct(LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'pg_adminProduct/delete.html'
    context_object_name = "products"
    form_class = ProductForm
    success_url = reverse_lazy("pg_adminProduct:product_list")
    login_url = "/login/"

def demon_img_View(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProductForm()
    return render(request, 'pg_adminProduct/pg_adminProduct.html', {'form': form})

#Añadir class Editar