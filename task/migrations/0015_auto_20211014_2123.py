# Generated by Django 3.2.8 on 2021-10-14 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0014_current_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completed',
            name='user',
        ),
        migrations.RemoveField(
            model_name='deleted',
            name='user',
        ),
    ]
