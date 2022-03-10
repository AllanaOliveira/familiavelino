from django.contrib import admin

# Register your models here.
from ide.models import Ide
from ide.models import ImagemIde

admin.site.register(Ide)
admin.site.register(ImagemIde)