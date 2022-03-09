from django.db import models

# Create your models here.
class ListaPresente(models.Model):
    class Meta:
        ordering = ('produto',)

    id = models.AutoField(primary_key=True)
    produto = models.CharField(max_length=200)
    descricao = models.TextField(default='')
    valor = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    presenteado_por = models.CharField(default='',max_length=180, blank=True)
    presente = models.BooleanField(default=0)
    foto = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/lista_presentes',
    )

    def get_absolute_url(self):
        return reverse('lista_presentes:exibe_presente', args=[self.id])
