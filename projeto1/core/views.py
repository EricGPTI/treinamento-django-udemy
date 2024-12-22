from django.shortcuts import render
from .models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é muito bom',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    #produto = get_object_or_404(Produto, id=pk)
    produto = Produto.objects.get(id=pk)
    return render(request, 'produto.html', {'produto': produto})


def error_404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8request', status=404)

def error_500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8request', status=500)
