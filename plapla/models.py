from django.db import models
from datetime import datetime

# Create your models here.
class Categoria(models.Model):
    class Meta:
        ordering = ('nome',)
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)

class Plapla(models.Model):
    class Meta:
        ordering = ('data_postagem', 'categoria',)

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    escrito_por = models.CharField(max_length=80)
    data_postagem = models.DateField(default=datetime.now, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE,)
    texto = models.TextField
    imagem = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/plapla',
    )
    link = models.URLField(null=True,blank=True)

