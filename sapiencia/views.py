from django.shortcuts import render

from sapiencia.models import Sapiencia

# Create your views here.
def index(request):
    sapiencias = Sapiencia.objects.all()
    return render(request, 'sapiencia/index.html', {'sapiencias': sapiencias })