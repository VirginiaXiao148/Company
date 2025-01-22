# Generated by Django 5.1.4 on 2025-01-21 20:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="leave",
            old_name="start_date",
            new_name="date",
        ),
        migrations.RemoveField(
            model_name="leave",
            name="leave_type",
        ),
        migrations.AddField(
            model_name="leave",
            name="start_time",
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="leave",
            name="end_date",
            field=models.TimeField(),
        ),
    ]
