# Generated by Django 3.2.3 on 2021-05-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='is_sensor_color',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Sensor de Cor'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='industrial',
            field=models.BooleanField(default=True, verbose_name='Sensor Industrial'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_color',
            field=models.CharField(blank=True, choices=[('v', 'Sem Cor'), ('r', 'Vermelho'), ('g', 'Verde'), ('b', 'Azul')], default='v', max_length=10, null=True, verbose_name='Valor inicial'),
        ),
    ]
