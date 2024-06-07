# Generated by Django 5.0.6 on 2024-05-11 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('total_prendas', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.cliente')),
            ],
        ),
    ]
