# Generated by Django 4.1 on 2022-12-17 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_comic_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comic',
            old_name='file',
            new_name='comicBook',
        ),
    ]