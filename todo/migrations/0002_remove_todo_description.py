# Generated by Django 4.1.13 on 2024-11-26 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
    ]
