# Generated by Django 5.0.4 on 2024-05-29 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountmodel",
            name="arroba",
            field=models.TextField(default="", max_length=20, unique=True),
        ),
    ]
