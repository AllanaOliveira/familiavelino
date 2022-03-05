from django.shortcuts import render

from pacto.models import Pacto

# Create your views here.
def index(request):
    pactos = Pacto.objects.all()
    return render(request, 'pacto/index.html', {'pactos': pactos })