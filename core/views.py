from django.shortcuts import render
from django.contrib import messages

from .forms import contatoForm
def index(request):
    return render(request, 'index.html')

def contato(request):
    form = contatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.changed_data['nome']
            email = form.changed_data['email']
            assunto = form.changed_data['assunto']
            mensagem = form.changed_data['mensagem']

            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'E-Mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.sucess(request, 'Email enviado com sucesso!')
            form = contatoForm()

        else:
            messages.error(request, 'Erro ao enviar email')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')