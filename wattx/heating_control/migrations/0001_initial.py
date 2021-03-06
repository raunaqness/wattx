# Generated by Django 4.0 on 2021-12-11 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomID', models.CharField(max_length=20)),
                ('motion_present', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Valve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valveID', models.CharField(max_length=20)),
                ('level', models.IntegerField(default=0)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heating_control.room')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensorID', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('temperature', 'temperature')], max_length=20)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heating_control.room')),
            ],
        ),
    ]
