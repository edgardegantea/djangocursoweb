# Generated by Django 4.1.7 on 2023-03-06 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_alter_libro_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='isbn',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='ISBN'),
        ),
    ]
