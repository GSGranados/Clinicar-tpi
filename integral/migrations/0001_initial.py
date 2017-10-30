# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 06:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enfermedad', models.CharField(help_text='Enfermedad que padece', max_length=32, verbose_name='Enfermedad')),
                ('familiar', models.BooleanField(default=False, verbose_name='¿Algún familiar también padece esta enfermedad?')),
                ('tratamiento', models.BooleanField(default=False, verbose_name='¿Le ha sido administrado algún tratamiento?')),
                ('medicamento_asignado', models.CharField(max_length=256, verbose_name='Medicamento asignado')),
            ],
            options={
                'verbose_name': 'Antecedente',
                'verbose_name_plural': 'Antecedentes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ConsultaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('hora', models.TimeField(verbose_name='Hora de Consulta')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso')),
                ('talla', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Talla')),
                ('ta', models.CharField(help_text='Tensión arterial ###/##', max_length=6, verbose_name='Tensión arterial')),
                ('fc', models.DecimalField(decimal_places=2, help_text='Frecuencia cardíaca', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Frecuencia cardíaca')),
                ('problema', models.CharField(help_text='Motivo de consulta', max_length=256, verbose_name='Historia del problema')),
                ('diagnostico', models.CharField(max_length=256, verbose_name='Diagnostico')),
                ('prox_control', models.DateTimeField(blank=True, null=True)),
                ('precio_consulta', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio de la Consulta')),
            ],
            options={
                'verbose_name': 'Cita Médica',
                'verbose_name_plural': 'Citas Médicas',
                'ordering': ['fecha', 'hora'],
            },
        ),
        migrations.CreateModel(
            name='DetalleReceta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento', models.CharField(max_length=256, verbose_name='Medicamento')),
                ('indicaciones', models.CharField(max_length=256, verbose_name='Indicaciones')),
            ],
            options={
                'verbose_name': 'Detalle de Receta',
                'verbose_name_plural': 'Detalles de Recetas',
                'ordering': ['fk_detalle_receta'],
            },
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_apertura', models.DateField(auto_now_add=True, verbose_name='Fecha de apertura')),
            ],
            options={
                'verbose_name': 'Expediente',
                'verbose_name_plural': 'Expedientes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombres del paciente')),
                ('apellido', models.CharField(max_length=40, verbose_name='Apellidos del paciente')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Sexo')),
                ('fecha_nacimiento', models.DateField(help_text='Formato: DD/MM/AAAA', verbose_name='Fecha de nacimiento')),
                ('telefono', models.CharField(help_text='Formato: XXXX-XXXX', max_length=9, unique=True, verbose_name='Número de teléfono')),
                ('direccion', models.CharField(help_text='Dirección de su residencia', max_length=80, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['expediente'],
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora de prescripción')),
                ('fk_receta_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integral.ConsultaMedica')),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
                'ordering': ['fecha_hora'],
            },
        ),
        migrations.AddField(
            model_name='expediente',
            name='paciente',
            field=models.OneToOneField(help_text='Expediente asignado', on_delete=django.db.models.deletion.CASCADE, to='integral.Paciente'),
        ),
        migrations.AddField(
            model_name='detallereceta',
            name='fk_detalle_receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integral.Receta'),
        ),
        migrations.AddField(
            model_name='consultamedica',
            name='fk_consulta_expediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integral.Expediente'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='fk_antecedente_expediente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='integral.Expediente'),
        ),
    ]
