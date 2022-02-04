# Generated by Django 4.0.2 on 2022-02-04 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.BigIntegerField()),
                ('manufacturer', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('regisration_number', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DailyVehicleUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mileage', models.BigIntegerField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle')),
            ],
        ),
    ]
