# Generated by Django 4.2.4 on 2023-08-09 12:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("planetarium", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="astronomyshow",
            old_name="show_theme",
            new_name="show_themes",
        ),
    ]
