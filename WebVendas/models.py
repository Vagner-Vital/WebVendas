from django.db import models


class empresa(models.Model):
    id = models.AutoField(primary_key=True)
    razao_social = models.CharField('Razão social', max_length=50, blank=True, unique=True)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=50, blank=False, unique=True)
    cnpj = models.CharField('Cnpj', max_length=20, blank=True, unique=False)
    inscricao_estadual = models.CharField('Inscrição estadual', max_length=20, blank=True)
    inscricao_municipal = models.CharField('Inscrição municipal', max_length=20, blank=True)
    telefone = models.CharField(max_length=30, blank=False)
    celular = models.CharField(max_length=30, blank=True)
    email = models.EmailField('E-mail', blank=False)
    site = models.CharField(max_length=50, blank=False)
    cep = models.CharField(max_length=9, blank=True)
    endereco = models.CharField(max_length=40, blank=False)
    numero = models.CharField(max_length=10, blank=False)
    complemento = models.CharField(max_length=30, blank=True)
    bairro = models.CharField(max_length=50, blank=False)
    cidade = models.CharField(max_length=50, blank=False)
    status = models.CharField('Status', max_length=20, blank=False, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('SUSPENSO', 'SUSPENSO'),
        ('EXCLUIDO', 'EXCLUIDO'),
        ('NEGATIVADO', 'NEGATIVADO'),
    ))

    data_inicio = models.DateField(blank=True, null=True)
    contrato = models.CharField('Contrato', max_length=30, blank=True)
    observacoes = models.TextField(max_length=250, blank=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_fantasia

    class Meta:
        db_table = 'empresas'
        ordering = ('nome_fantasia',)
