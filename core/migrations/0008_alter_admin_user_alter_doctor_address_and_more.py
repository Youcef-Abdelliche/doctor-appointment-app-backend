# Generated by Django 4.1.4 on 2023-01-01 20:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_remove_admin_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="address",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="address",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="patient",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
