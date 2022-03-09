from django.db import models
from datetime import datetime

# Create your models here.
class Ide(models.Model):
    class Meta:
        ordering = ('data_postagem',)

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    data_postagem = models.DateField(default=datetime.now, blank=True)
    texto = models.TextField


class ImagemIde(models.Model):
    """Cada instancia desta classe contem uma imagem da galeria, com seu
    respectivo thumbnail (miniatura) e imagem em tamanho natural.
    Varias imagens podem conter dentro de um Album"""

    class Meta:
        ordering = ('ide', 'titulo')

    ide = models.ForeignKey('Ide', on_delete=models.CASCADE, default=1)
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    descricao = models.TextField(blank=True)
    foto = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/pacto',
    )

    def __unicode__(self):
        return self.titulo
