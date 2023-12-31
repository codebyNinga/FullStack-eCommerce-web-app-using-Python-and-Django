# Generated by Django 4.1 on 2022-08-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comic_is_featured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': '1. Banners'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '2. Categories'},
        ),
        migrations.AlterModelOptions(
            name='comic',
            options={'verbose_name_plural': '4.Comics'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name_plural': '3.Publishers'},
        ),
        migrations.AddField(
            model_name='comic',
            name='file',
            field=models.FileField(default=models.ImageField(upload_to='comic_imgs/'), upload_to='comic_files/'),
        ),
    ]
