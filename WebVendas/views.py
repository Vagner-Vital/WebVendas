from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
from django.urls import reverse_lazy
from .models import empresa, cliente


class empresaCreateView(CreateView):
    form_class = empresa
    template_name = 'cadastrar/empresa.html'

    def get_success_url(self):
        messages.success(self.request, 'Empresa cadastrada com suceso!')
        return reverse_lazy("listar_empresa")


class clienteCreateView(CreateView):
    form_class = cliente
    template_name = 'cadastrar/cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'cliente cadastrado com suceso!')
        return reverse_lazy("listar_cliente")






def cadastrar_empresa(request):
    return render(request, "form.html")


def cadastrar_cliente(request):
    return render(request, "form.html")
