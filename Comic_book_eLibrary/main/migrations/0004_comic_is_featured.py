# Generated by Django 4.1 on 2022-08-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
