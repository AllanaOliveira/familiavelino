from django.db import models

# Create your models here.
class Ebook(models.Model):
    class Meta:
        ordering = ('titulo',)

    id = models.BigIntegerField(primary_key=True)
    titulo = models.CharField(max_length=80)
    prefacio = models.TextField
    imagem = models.FileField(
            null=True,
            blank=True,
            upload_to='galeria/ebook',
        )
    pdf = models.FileField(
        null=True,
        blank=True,
        upload_to='documento/ebook',
    )
