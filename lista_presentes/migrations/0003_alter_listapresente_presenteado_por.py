# Generated by Django 4.0.1 on 2022-03-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_presentes', '0002_listapresente_descricao_listapresente_presente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listapresente',
            name='presenteado_por',
            field=models.CharField(default='', max_length=180, null=True),
        ),
    ]
