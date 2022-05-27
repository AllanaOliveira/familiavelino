from django.contrib import admin

# Register your models here.
from lista_presentes.models import ListaPresente

admin.site.site_header = 'Admin Família Avelino'

class ListaPresenteAdmin(admin.ModelAdmin):
    list_display = ('produto', 'presenteado_por')

admin.site.register(ListaPresente, ListaPresenteAdmin)
