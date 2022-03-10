from django.shortcuts import render, get_object_or_404

from ide.models import Ide
from ide.models import ImagemIde

# Create your views here.
def index(request):
    ides = Ide.objects.all()
    imagens_ide = ImagemIde.objects.all()
    return render(request, 'ide/index.html', {'ides': ides, 'imagens_ide': imagens_ide })

def show(request, id):
    ide = get_object_or_404(Ide, pk=id)
    texto = ide.texto.split('</br>')
    return render(request, 'ide/show.html', {'ide': ide, 'texto': texto})