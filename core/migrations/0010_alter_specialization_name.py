# Generated by Django 4.1.4 on 2023-01-02 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_alter_user_sex"),
    ]

    operations = [
        migrations.AlterField(
            model_name="specialization",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
