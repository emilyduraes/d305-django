from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, './base.html')

def inicio(request):
    lista_autores = ['Autor 1', 'Autor 2', 'Autor 3', 'Autor 4']
    lista_noticias = ['Notícia 1', 'Notícia 2', 'Notícia 3', 'Notícia 4']
    
    parametros = {
        'Autor': lista_autores,
        'Noticias': lista_noticias
    }

    return render(request, './index.html', parametros)

def autores(request):
    return render(request, './autores.html')

def noticias(request):
    return render(request, './noticias.html')