# Generated by Django 3.2.8 on 2021-10-14 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0011_auto_20211014_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='completed',
            name='status',
            field=models.CharField(choices=[('Current', 'Current'), ('Completed', 'Completed'), ('Deleted', 'Deleted')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Deleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Current', 'Current'), ('Completed', 'Completed'), ('Deleted', 'Deleted')], max_length=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Deleted',
            },
        ),
    ]