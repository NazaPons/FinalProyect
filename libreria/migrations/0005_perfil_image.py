# Generated by Django 4.1 on 2022-10-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_delete_postarticulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
