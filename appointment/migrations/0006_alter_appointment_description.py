# Generated by Django 4.1.4 on 2023-01-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointment", "0005_appointment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]