from django.db import models

# Create your models here.
class Origem(models.Model):
    class Meta:
        ordering = ('titulo',)

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    texto = models.TextField(blank=True)
