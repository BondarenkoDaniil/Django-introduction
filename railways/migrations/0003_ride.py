# Generated by Django 2.1.4 on 2019-01-08 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0002_train'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('amount', models.PositiveIntegerField()),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railways.Route')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railways.Train')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]