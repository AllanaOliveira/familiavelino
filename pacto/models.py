from django.db import models

# Create your models here.
class Pacto(models.Model):
    class Meta:
        ordering = ('titulo',)

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    texto = models.TextField


class ImagemPacto(models.Model):
    """Cada instancia desta classe contem uma imagem da galeria, com seu
    respectivo thumbnail (miniatura) e imagem em tamanho natural.
    Varias imagens podem conter dentro de um Album"""

    class Meta:
        ordering = ('pacto', 'titulo',)

    pacto = models.ForeignKey('Pacto', on_delete=models.CASCADE,)
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
