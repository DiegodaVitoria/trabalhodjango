from django.shortcuts import render
from .models import Usuario
from .forms import ClienteForm


def index(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirma.html')
        else:
            form = ClienteForm()
    else:
        form = ClienteForm()
    return render(request, 'index.html', {'form': form})


def list(request):
    pessoa = Usuario.objects.all()
    context = {
        'pessoa': pessoa
    }
    return render(request, 'list.html', context)

def confirma(request):

    return render(request, 'confirma.html')