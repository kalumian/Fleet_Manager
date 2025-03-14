# Generated by Django 5.1.7 on 2025-03-11 08:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('available_hours', models.FloatField(default=70)),
                ('hours_used_last_8_days', models.FloatField(default=0)),
                ('hours_remaining_today', models.FloatField(default=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('planned', 'Planned'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='planned', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('current_cycle_hours_used', models.FloatField(default=0)),
                ('estimated_distance', models.FloatField(default=0)),
                ('estimated_duration', models.FloatField(default=0)),
                ('actual_distance', models.FloatField(blank=True, null=True)),
                ('actual_duration', models.FloatField(blank=True, null=True)),
                ('current_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_current', to='trips.location')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.driver')),
                ('dropoff_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_dropoff', to='trips.location')),
                ('pickup_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_pickup', to='trips.location')),
            ],
        ),
        migrations.CreateModel(
            name='RouteStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_type', models.CharField(choices=[('rest', 'Rest Stop'), ('fuel', 'Fuel Stop'), ('food', 'Food Stop'), ('overnight', 'Overnight Stop')], max_length=20)),
                ('planned_arrival', models.DateTimeField()),
                ('planned_departure', models.DateTimeField()),
                ('actual_arrival', models.DateTimeField(blank=True, null=True)),
                ('actual_departure', models.DateTimeField(blank=True, null=True)),
                ('distance_from_last_stop', models.FloatField(default=0)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.location')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='trips.trip')),
            ],
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('off_duty', 'Off Duty'), ('sleeper_berth', 'Sleeper Berth'), ('driving', 'Driving'), ('on_duty', 'On Duty Not Driving')], max_length=20)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('total_driving_hours', models.FloatField(default=0)),
                ('total_off_duty_hours', models.FloatField(default=0)),
                ('total_sleeper_berth_hours', models.FloatField(default=0)),
                ('total_on_duty_hours', models.FloatField(default=0)),
                ('total_miles_today', models.FloatField(default=0)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.driver')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_entries', to='trips.trip')),
            ],
        ),
    ]
