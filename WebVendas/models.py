from django.db import models


# ___________________________________________Class Empresa____________________________________
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


# ___________________________________________Class Cliente____________________________________
class cliente(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=50, blank=False)
    sobrenome = models.CharField('Sobrenome', max_length=50, blank=True)
    cpf = models.CharField('Cpf', max_length=11, blank=False)
    rg = models.CharField('Rg', max_length=15, blank=True)
    telefone = models.CharField('Telefone', max_length=30, blank=True)
    celular = models.CharField('Celular', max_length=30, blank=True)
    email = models.EmailField('E-mail', blank=False, unique=True)
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
        ('AFASTADO', 'AFASTADO'),
        ('APOSENTADO', 'APOSENTADO'),
        ('DEMITIDO', 'DEMITIDO'),
    ))
    foto_Perfil = models.FileField(upload_to='outro_diretorio/', null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=50, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=30, blank=True)
    bairro = models.CharField('Bairro', max_length=50, blank=True)
    cidade = models.CharField('Cidade', max_length=50, blank=False)
    cep = models.CharField('CEP', max_length=10, blank=True)
    estado = models.CharField('Estado', max_length=2, blank=False)
    sexo = models.CharField('Sexo', max_length=10, choices=(
        ('MASCULINO', 'MASCULINO'),
        ('FEMININO', 'FEMININO'),
        ('OUTROS', 'OUTROS'),
    ))
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    model_template = models.CharField(max_length=20, blank=True)
    observacoes = models.TextField('Observações', max_length=200, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'clientes'
        ordering = ('nome',)
