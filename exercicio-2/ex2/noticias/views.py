from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, './index.html')

def autores(request):
    return render(request, './autores.html')

def noticias(request):
    return render(request, './noticias.html')
