# Generated by Django 4.1.5 on 2023-01-29 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_galleryshelf_gallerycollection'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GalleryCollection',
        ),
        migrations.DeleteModel(
            name='GalleryShelf',
        ),
    ]
