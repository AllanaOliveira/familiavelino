from django.shortcuts import render

from ide.models import Ide

# Create your views here.
def index(request):
    ides = Ide.objects.all()
    return render(request, 'ide/index.html', {'ides': ides })