# Generated by Django 5.1.4 on 2025-01-21 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0004_remove_shift_actions_alter_leave_actions"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="leave",
            name="end_time",
        ),
        migrations.RemoveField(
            model_name="leave",
            name="start_time",
        ),
    ]
