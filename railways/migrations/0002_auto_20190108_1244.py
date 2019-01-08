# Generated by Django 2.1.4 on 2019-01-08 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('railways', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railways.Ride'),
        ),
        migrations.AddField(
            model_name='routeitem',
            name='previous_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='railways.RouteItem'),
        ),
        migrations.AddField(
            model_name='routeitem',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='railways.Route'),
        ),
        migrations.AddField(
            model_name='routeitem',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='railways.Track'),
        ),
        migrations.AddField(
            model_name='route',
            name='arrival_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes_arrival', to='railways.Station'),
        ),
        migrations.AddField(
            model_name='route',
            name='departure_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes_departure', to='railways.Station'),
        ),
        migrations.AddField(
            model_name='ride',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railways.Route'),
        ),
    ]
