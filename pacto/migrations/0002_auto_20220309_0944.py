# Generated by Django 2.2.dev20180912221234 on 2022-03-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagempacto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
