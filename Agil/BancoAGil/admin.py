from django.contrib import admin
from .models import Cpf, Empresa

# Register your models here.
class CpfAdmin(admin.ModelAdmin):
    # Define quais campos devem ser exibidos na lista
    list_display = ('cpf', 'email', 'data_armazenamento', 'hora_armazenamento')
    
    # Adiciona filtros para os campos desejados
    list_filter = ('data_armazenamento', 'hora_armazenamento')
    
    # Adiciona campos de busca
    search_fields = ('cpf', 'email', )
    
    # Define a ordenação padrão na lista
    ordering = ('-data_armazenamento', '-hora_armazenamento')
    
    # Permite a seleção de múltiplos itens e a visualização em página
    list_per_page = 20

    # Adiciona uma visualização detalhada com campos de visualização específicos
    fields = ('cpf', 'email', 'data_armazenamento', 'hora_armazenamento')
    readonly_fields = ('data_armazenamento', 'hora_armazenamento')

admin.site.register(Cpf, CpfAdmin)










class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'cnpj', 'status', 'data_abertura')
    search_fields = ('nome_fantasia', 'cnpj', 'status')
    list_filter = ('status', 'data_abertura', 'uf')
    ordering = ('-data_abertura',)

admin.site.register(Empresa, EmpresaAdmin)