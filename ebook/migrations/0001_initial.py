# Generated by Django 4.0.1 on 2022-03-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=80)),
                ('imagem', models.FileField(blank=True, null=True, upload_to='galeria/ebook')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='documento/ebook')),
            ],
            options={
                'ordering': ('titulo',),
            },
        ),
    ]
