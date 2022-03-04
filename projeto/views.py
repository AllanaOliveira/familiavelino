from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def origem(request):
    return render(request, 'origem.html')