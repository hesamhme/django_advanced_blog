# Generated by Django 5.1 on 2024-09-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_verifeid",
            field=models.BooleanField(default=False),
        ),
    ]
