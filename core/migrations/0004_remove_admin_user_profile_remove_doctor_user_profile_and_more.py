# Generated by Django 4.1.4 on 2023-01-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_userprofile_sex"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="admin",
            name="user_profile",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="user_profile",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="user_profile",
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="admin",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="sex",
            field=models.CharField(
                choices=[("M", "male"), ("F", "female")], default="M", max_length=1
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="patient",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
