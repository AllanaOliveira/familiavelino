from django.shortcuts import render

from plapla.models import Plapla

# Create your views here.
def index(request):
    plapla = Plapla.objects.all()
    return render(request, 'plapla/index.html', {'plapla': plapla })