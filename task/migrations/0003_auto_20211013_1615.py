# Generated by Django 3.2.8 on 2021-10-13 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20211013_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='completed',
            options={'verbose_name': 'Completed'},
        ),
        migrations.AlterModelOptions(
            name='current',
            options={'verbose_name': 'Current'},
        ),
        migrations.RenameField(
            model_name='current',
            old_name='tasks',
            new_name='task',
        ),
    ]
