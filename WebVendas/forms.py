from django import forms
from .models import *


class empresaForms(forms.ModelForm):
    class Meta:
        model = empresa
        fields = ['id', 'razao_social', 'nomefantaia', 'cnpj', 'inscricao_estadual', 'inscricao_municipal',
                  'telefone', 'celular', 'email', 'endereço', 'cidade']


class clienteForms(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['id', 'nome ', 'sobrenome ', 'cpf', 'rg', 'telefone',
                  'celular', 'email', 'endereço', 'cidade', 'sexo']
