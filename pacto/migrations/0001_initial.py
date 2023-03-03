# Generated by Django 4.0.1 on 2022-03-01 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=80)),
            ],
            options={
                'ordering': ('titulo',),
            },
        ),
        migrations.CreateModel(
            name='ImagemPacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('descricao', models.TextField(blank=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='galeria/ide')),
                ('ide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ide.ide')),
            ],
            options={
                'ordering': ('ide', 'titulo'),
            },
        ),
    ]
