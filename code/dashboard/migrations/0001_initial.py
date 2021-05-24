# Generated by Django 3.2.3 on 2021-05-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
                ('industrial', models.BooleanField(default=True)),
                ('sensor_color', models.CharField(blank=True, choices=[('v', 'Sem Cor'), ('r', 'Vermelho'), ('g', 'Verde'), ('b', 'Azul')], default='v', max_length=10, null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
