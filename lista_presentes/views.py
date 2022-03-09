from django.shortcuts import render, get_object_or_404

from lista_presentes.models import ListaPresente
from lista_presentes.forms import ListaPresenteForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    lista_presentes = ListaPresente.objects.all()
    return render(request, 'lista_presentes/index.html', {'lista_presentes': lista_presentes })

def exibe_salva_presente(request, id):
    lista_presentes = get_object_or_404(ListaPresente, pk=id)
    msg = ''
    if request.POST:
        lista_presentes.presenteado_por = request.POST['presenteado_por']
        lista_presentes.presente = True
        lista_presentes.save()
        msg = 'Você conseguiu presentear com sucesso. Muito obrigado pelo carinho conosco! Entre em contato para definir a forma de recebimento do presente.'
    form = ListaPresenteForm()
    request.session['lista_presentes_id_del'] = id
    contexto = {
        'form': form, 'msg': msg, 'presente': lista_presentes
    }
    return render(request, 'lista_presentes/exibe_salva_presente.html', contexto)