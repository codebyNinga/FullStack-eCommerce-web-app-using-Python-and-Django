# Generated by Django 4.1 on 2022-12-15 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_comic_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comic',
            old_name='user',
            new_name='vendor',
        ),
    ]