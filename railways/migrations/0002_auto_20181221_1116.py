# Generated by Django 2.1.4 on 2018-12-21 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routeitem',
            name='previous_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='railways.RouteItem'),
        ),
    ]
