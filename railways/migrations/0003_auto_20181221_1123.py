# Generated by Django 2.1.4 on 2018-12-21 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0002_auto_20181221_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routeitem',
            name='previous_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='railways.RouteItem'),
        ),
    ]
