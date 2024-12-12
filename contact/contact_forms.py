from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import ContactForm


def create(request):
    #if request.method == 'POST':
    #    print(request.POST.get('first_name'))
    # print(request.method)
    # o método pode ser GET(ler) ou POST(criar ou postar)
    # é recomendado ter um if pro method, caso desa get fazer algo, caso seja post fazer outro
    #print(request.POST.get('first_name'))
    # Essa linha retorna o que foi no input do form. Cada input precisa ter um name unico, é assim que pegamos eles nos forms/views
    #<form> possui metodo POST
    #print(request.method)
    
    context = {
        'form': ContactForm()
    }

    return render(
        request, 
        'contact/create.html',
        context
    )
