# Generated by Django 3.2.8 on 2021-10-13 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20211013_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='completed',
            options={'verbose_name': 'Completeds'},
        ),
        migrations.AlterModelOptions(
            name='current',
            options={'verbose_name': 'Currents'},
        ),
    ]
