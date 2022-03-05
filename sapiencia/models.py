from django.db import models
from datetime import datetime

# Create your models here.
class Sapiencia(models.Model):
    class Meta:
        ordering = ('data_postagem',)

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    escrito_por = models.CharField(max_length=80)
    data_postagem = models.DateField(default=datetime.now, blank=True)
    texto = models.TextField
    imagem = models.ImageField(
            null=True,
            blank=True,
            upload_to='galeria/sapiencia',
        )