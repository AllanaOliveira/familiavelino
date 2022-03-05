from django import forms
from lista_presentes.models import ListaPresente

class ListaPresenteForm(forms.Form):
    class ListaPresente:
        fields= ('presenteado_por', 'presente')
    presenteado_por = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome para presentear...'}), label='presenteado_por',max_length=180)
    presente = forms.BooleanField(label='presente')
