# Generated by Django 4.2 on 2024-08-05 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_manager', '0002_remove_album_ano_lanzamiento_album_año_lanzamiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='año_lanzamiento',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='album',
            name='genero',
            field=models.CharField(max_length=50),
        ),
    ]
