from django.shortcuts import render

from origem.models import Origem

# Create your views here.
def origem(request):
    origens = Origem.objects.all()
    return render(request, 'origem/origem.html', {'origens': origens })