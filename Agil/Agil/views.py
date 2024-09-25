from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .Utils import EmailSender, process_email, buscar_cnpj, limpar_cnpj, Process_cnpj



def ValidCpfOrCnpj(identificador, Empresa, Setor, nome, email, mensagem, cnpj, cpf):
    if cnpj:
        Acnpj = limpar_cnpj(cnpj)
        ListResult = buscar_cnpj(Acnpj)
        if ListResult:
            return Process_cnpj(ListResult, email, mensagem)
        return 'erro ao enviar email!'

    if cpf:
        return process_email(identificador, cpf, Empresa, Setor, nome, email, mensagem)

    return 'erro ao enviar email!'

def index(request):
    if request.method == 'POST':
        identificador = request.POST['identification']
        Empresa = request.POST['companyName']
        Setor = request.POST['sector']
        nome = request.POST['name']
        email = request.POST['email']
        mensagem = request.POST['message']
        cnpj = request.POST['cnpj']
        cpf = request.POST['cpf']

        # Processar e obter o resultado
        resultado = ValidCpfOrCnpj(identificador, Empresa, Setor, nome, email, mensagem, cnpj, cpf)

        # Redirecionar com base no resultado
        if resultado == 'validado, criado e enviado com sucesso':
            return render(request, 'index.html', {'SendEmailTrue': True})
        elif resultado == 'Cnpj Ja existe!':
            return render(request, 'index.html', {'solicitAproved': True})
        elif resultado == 'erro ao enviar email!':
            return render(request, 'index.html', {'SendEmailFalse': True})
        elif resultado == 'email não e válido':
            return render(request, 'index.html', {'EmailInvalido': True})
        elif resultado == 'cpf já existe':
            return render(request, 'index.html', {'solicitAproved': True})
        elif resultado == 'validado e criado com sucesso':
            return render(request, 'index.html', {'SendEmailTrue': True})
        elif resultado == 'Erro ao enviar Email':
            return render(request, 'index.html', {'SendEmailFalse': True})
        else:
            return render(request, 'index.html', {'SendEmailFalse': True})

    return render(request, 'index.html')

def __PaginaFlex(request):
    if request.method == 'POST':
        identificador = request.POST['identification']
        Empresa = request.POST['companyName']
        Setor = request.POST['sector']
        nome = request.POST['name']
        email = request.POST['email']
        mensagem = request.POST['message']
        cnpj = request.POST['cnpj']
        cpf = request.POST['cpf']

        # Processar e obter o resultado
        resultado = ValidCpfOrCnpj(identificador, Empresa, Setor, nome, email, mensagem, cnpj, cpf)

        # Redirecionar com base no resultado
        if resultado == 'validado, criado e enviado com sucesso':
            return render(request, 'flexOnline.html', {'SendEmailTrue': True})
        elif resultado == 'Cnpj Ja existe!':
            return render(request, 'flexOnline.html', {'solicitAproved': True})
        elif resultado == 'erro ao enviar email!':
            return render(request, 'flexOnline.html', {'SendEmailFalse': True})
        elif resultado == 'email não e válido':
            return render(request, 'flexOnline.html', {'EmailInvalido': True})
        elif resultado == 'cpf já existe':
            return render(request, 'flexOnline.html', {'solicitAproved': True})
        elif resultado == 'validado e criado com sucesso':
            return render(request, 'flexOnline.html', {'SendEmailTrue': True})
        elif resultado == 'Erro ao enviar Email':
            return render(request, 'flexOnline.html', {'SendEmailFalse': True})
        else:
            return render(request, 'flexOnline.html', {'SendEmailFalse': True})

    return render(request, 'flexOnline.html')

def _inscreverEmail(request):
    if request.method =='POST':
        Email = request.POST['Email']
        try:
            emailSenderVar =EmailSender()
            emailSenderVar.send_inscrever_email(Email)            
            return render(request, 'index.html', {'SendEmailTrue': True})
        except Exception as e:
            print(e)
            return render(request, 'index.html', {'SendEmailFalse': True})
    # Adicionando uma resposta padrão para métodos que não sejam POST
    return render(request, 'index.html')
            
    

