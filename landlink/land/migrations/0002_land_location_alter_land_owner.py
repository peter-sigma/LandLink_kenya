# Generated by Django 5.0.2 on 2024-02-15 13:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='location',
            field=models.CharField(blank=True, help_text="Enter the latitude and longitude coordinates (e.g., 'latitude,longitude') for the location of the land.", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='owner',
            field=models.ForeignKey(limit_choices_to={'user_type': 'seller'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
