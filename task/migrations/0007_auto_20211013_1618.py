# Generated by Django 3.2.8 on 2021-10-13 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20211013_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='completed',
            options={'verbose_name': 'Completed', 'verbose_name_plural': 'Completed'},
        ),
        migrations.AlterModelOptions(
            name='current',
            options={'verbose_name': 'Current', 'verbose_name_plural': 'Current'},
        ),
    ]