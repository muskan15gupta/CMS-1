# Generated by Django 3.2.19 on 2024-06-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predictioninput',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='predictioninput',
            name='prediction_co2_emissions',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictioninput',
            name='prediction_electricity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictioninput',
            name='prediction_gdp_growth',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictioninput',
            name='prediction_renewables_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
