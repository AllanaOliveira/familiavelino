# Generated by Django 4.0.1 on 2022-03-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_presentes', '0003_alter_listapresente_presenteado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listapresente',
            name='presenteado_por',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
    ]
