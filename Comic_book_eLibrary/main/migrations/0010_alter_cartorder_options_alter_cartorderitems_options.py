# Generated by Django 4.1 on 2022-11-05 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_cartorder_cartorderitems'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartorder',
            options={'verbose_name_plural': '5. Orders'},
        ),
        migrations.AlterModelOptions(
            name='cartorderitems',
            options={'verbose_name_plural': '6. Order Items'},
        ),
    ]