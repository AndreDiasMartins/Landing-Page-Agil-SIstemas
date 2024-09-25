from django.db import models





class Cpf(models.Model):
    id = models.AutoField(primary_key=True)
    data_armazenamento = models.DateField(auto_now_add=True)
    hora_armazenamento = models.TimeField(auto_now_add=True)
    cpf = models.CharField(max_length=14, null=True, blank=True, unique=True)
    email = models.CharField(max_length=254, default='no-reply@example.com')


    def __str__(self):
        return self.cpf if self.cpf else ''

class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)  # CNPJ no formato 'XX.XXX.XXX/0001-XX'
    status = models.CharField(max_length=100)
    cnae_principal_descricao = models.CharField(max_length=255)
    cnae_principal_codigo = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)  # CEP no formato 'XXXXX-XXX'
    data_abertura = models.CharField(max_length=20)
    ddd = models.CharField(max_length=3)  # DDD da localidade
    telefone = models.CharField(max_length=15)  # Telefone no formato '(XX) XXXXX-XXXX'
    email = models.EmailField()
    tipo_logradouro = models.CharField(max_length=120)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)  # UF do estado, por exemplo, 'SP'

    def __str__(self):
        return self.nome_fantasia
