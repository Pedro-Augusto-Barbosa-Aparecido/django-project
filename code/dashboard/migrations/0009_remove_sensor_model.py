# Generated by Django 3.2.3 on 2021-05-23 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_rename_values_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='model',
        ),
    ]
