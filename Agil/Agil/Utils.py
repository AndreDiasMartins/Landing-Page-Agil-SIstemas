import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from django.template.loader import render_to_string
from email_validator import validate_email, EmailNotValidError 
from BancoAGil.models import Cpf, Empresa
import requests
from django.core.exceptions import ValidationError
import re


class EmailSender:
    def __init__(self):
        # Configurações do servidor SMTP
        self.server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        self.from_email = settings.EMAIL_HOST_USER

    def __send_email(self, to_email, template_name, context, subject):
        # Criação da mensagem
        html_message = render_to_string(template_name, context)
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = self.from_email
        msg["To"] = to_email
        msg.attach(MIMEText(html_message, "html"))

        # Enviar o email
        self.server.sendmail(self.from_email, to_email, msg.as_string())

    def send_emails(self, identificador,cpf,  Empresa, Setor, nome, email, mensagem):
        try:
            # Enviar e-mail principal
            self.__send_email(
                to_email=self.from_email,
                template_name='SendEmailTemplate.html',
                context={
                    'identificador': identificador,
                    'cpf': cpf,
                    'Empresa': Empresa,
                    'Setor': Setor,
                    'nome': nome,
                    'email': email,
                    'mensagem': mensagem
                },
                subject=f"Solicitação {Empresa}"
            )
            
            # Enviar e-mail para cliente
            self.__send_email(
                to_email=email,
                template_name='SendEmailCliente.html',
                context={'nome': nome},
                subject="Assunto do Email"
            )
        finally:
            self.close()
            
    def send_emails_cnpj(self, dados, email, mensagem):
        try:
            # Enviar e-mail principal
            self.__send_email(
                to_email=self.from_email,
                template_name='SendEmailcnpj.html',
                context={
                    'nome_fantasia': dados[0],
                    'razao_social': dados[1],
                    'cnpj': dados[2],
                    'status': dados[3],
                    'cnae_principal_descricao': dados[4],
                    'cnae_principal_codigo': dados[5],
                    'cep': dados[6],
                    'data_abertura': dados[7],
                    'ddd': dados[8],
                    'telefone': dados[9],
                    'email': dados[10],
                    'tipo_logradouro': dados[11],
                    'logradouro': dados[12],
                    'numero': dados[13],
                    'complemento': dados[14],
                    'bairro': dados[15],
                    'municipio': dados[16],
                    'uf': dados[17],
                    'mensagem': mensagem,
                    'emailSolicitado' : email
                },
                subject=f"Solicitação {[dados[0] if dados[0] != 'Não declarado' else 'Cliente'][0]}"
            )
            
            # Enviar e-mail para cliente
            self.__send_email(
                to_email=email,
                template_name='SendEmailCliente.html',
                context={'nome': dados[0]},
                subject="Assunto do Email"
            )
        finally:
            self.close()
            
    def send_inscrever_email(self, email):
        try:
            self.__send_email(
                to_email=self.from_email,
                template_name='SendEmailInscrever.html',
                context={'email': email},
                subject="Email Capturado!"
            )
        finally:
            self.close()

    def close(self):
        self.server.quit()

    
def process_email(identificador, cpf,  empresa, Setor, nome, email, mensagem):
    # Primeiro, valida o formato do e-mail
    try:
        validate_email(email)
    except EmailNotValidError:
        return 'email não e válido'  # Retorna False se o e-mail não for válido
    
    
    # Verifica se o e-mail já existe no banco de dados
    if Cpf.objects.filter(cpf=cpf).exists():
        return 'cpf já existe'  # Retorna False se o e-mail já existir
    
    try:
        emailSenderVar =EmailSender()
        emailSenderVar.send_emails(identificador, cpf,  empresa, Setor, nome, email, mensagem)
    except Exception as e:
        return 'Erro ao enviar Email'

    # Cria um novo registro de e-mail no banco de dados
    Cpf.objects.create(cpf= cpf, email= email)
    return 'validado e criado com sucesso'  # Retorna True se o e-mail foi validado e criado com sucesso



def Process_cnpj(empresa: list, email: str, mensagem: str,) -> str:
    # Verifica se o e-mail já existe no banco de dados
    if Empresa.objects.filter(cnpj=empresa[2]).exists():
        return 'Cnpj Ja existe!' # Retorna False se o e-mail já existir
    else:
        try:
            EmailSender().send_emails_cnpj(dados=empresa, email=email, mensagem=mensagem)
        except Exception as e:
            return 'erro ao enviar email!'
        # Cria um novo registro de e-mail no banco de dados
        InstanceEmpresa = Empresa(
            nome_fantasia = empresa[0],
            razao_social = empresa[1],
            cnpj = empresa[2],
            status = empresa[3],
            cnae_principal_descricao = empresa[4],
            cnae_principal_codigo = empresa[5],
            cep = empresa[6],
            data_abertura = empresa[7],
            ddd = empresa[8],
            telefone = empresa[9],
            email = empresa[10],
            tipo_logradouro = empresa[11],
            logradouro = empresa[12],
            numero = empresa[13],
            complemento = empresa[14],
            bairro = empresa[15],
            municipio = empresa[16],
            uf = empresa[17],
        )
        InstanceEmpresa.save()
        return 'validado, criado e enviado com sucesso'  # Retorna True se o e-mail foi validado e criado com sucesso
    

def buscar_cnpj(cnpj):
    url = f'https://api-publica.speedio.com.br/buscarcnpj?cnpj={cnpj}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP 4xx/5xx
        dados = response.json()  # Converte a resposta em JSON
        if dados:
            def substituir_vazio(valor):
                return valor if valor != '' else 'Não declarado'
            # Atribuindo os valores do dicionário a variáveis
            nome_fantasia = substituir_vazio(dados.get('NOME FANTASIA', ''))
            razao_social = substituir_vazio(dados.get('RAZAO SOCIAL', ''))
            cnpj = substituir_vazio(dados.get('CNPJ', ''))
            status = substituir_vazio(dados.get('STATUS', ''))
            cnae_principal_descricao = substituir_vazio(dados.get('CNAE PRINCIPAL DESCRICAO', ''))
            cnae_principal_codigo = substituir_vazio(dados.get('CNAE PRINCIPAL CODIGO', ''))
            cep = substituir_vazio(dados.get('CEP', ''))
            data_abertura = substituir_vazio(dados.get('DATA ABERTURA', ''))
            ddd = substituir_vazio(dados.get('DDD', ''))
            telefone = substituir_vazio(dados.get('TELEFONE', ''))
            email = substituir_vazio(dados.get('EMAIL', ''))
            tipo_logradouro = substituir_vazio(dados.get('TIPO LOGRADOURO', ''))
            logradouro = substituir_vazio(dados.get('LOGRADOURO', ''))
            numero = substituir_vazio(dados.get('NUMERO', ''))
            complemento = substituir_vazio(dados.get('COMPLEMENTO', ''))
            bairro = substituir_vazio(dados.get('BAIRRO', ''))
            municipio = substituir_vazio(dados.get('MUNICIPIO', ''))
            uf = substituir_vazio(dados.get('UF', ''))
                        
            return [nome_fantasia, razao_social, cnpj, status, cnae_principal_descricao, cnae_principal_codigo, cep, data_abertura, ddd, telefone, email, tipo_logradouro, logradouro, numero, complemento, bairro, municipio, uf]
        else: return []
    except requests.RequestException as e:
        print(f'Erro ao fazer a solicitação: {e}')
        return None
    except ValueError as e:
        print(f'Erro ao converter resposta para JSON: {e}')
        return None


def limpar_cnpj(cnpj):
    return ''.join(char for char in cnpj if char.isdigit())


def limpar_cpf(cpf):
    """
    Remove pontos e hífens do CPF, deixando apenas números.
    """
    cpf_limpo = re.sub(r'[^\d]', '', cpf)
    return cpf_limpo

