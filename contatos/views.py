from django.shortcuts import render, redirect
from .models import Contato
from .forms import ContatoForm


def contatos_list(request):
    contatos = Contato.objects.all()
    context = {
        'contatos': contatos
    }

    return render(request, 'contatos/contatos_list.html', context=context)


def contato_create(request):
    if request.method == 'POST':
        contato_form = ContatoForm(request.POST)
        if contato_form.is_valid():
            contato_form.save()
            return redirect('contatos:list')
    else:
        contato_form = ContatoForm()
        context = {
            'form': contato_form
        }
        return render(request, 'contatos/contato_form.html', context=context)


def contato_update(request, pk):
    contato = Contato.objects.get(id=pk)
    if request.method == 'POST':
        contato_form = ContatoForm(request.POST, instance=contato)
        if contato_form.is_valid():
            contato_form.save()
            return redirect('contatos:list')
    else:
        contato_form = ContatoForm(instance=contato)
        context = {
            'form': contato_form,
            'contato': contato
        }
        return render(request, 'contatos/contato_form.html', context=context)


def contato_delete(request, pk):
    contato = Contato.objects.get(id=pk)
    if request.method == 'POST':
        contato.delete()
        return redirect('contatos:list')
    else:
        context = {
            'contato': contato
        }
        return render(request, 'contatos/contato_delete.html', context=context)


def contato_redirect(request, contato_id):
    if contato_id:
        return redirect('contatos:update', pk=contato_id)
    else:
        return redirect('contatos:create')
        