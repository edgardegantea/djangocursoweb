# Generated by Django 4.1.7 on 2023-02-27 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_alter_libro_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='images/libro/portadas/', verbose_name='Portada de libro'),
        ),
    ]