# Generated by Django 5.1.4 on 2025-01-21 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "management",
            "0002_rename_start_date_leave_date_remove_leave_leave_type_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="leave",
            old_name="reason",
            new_name="actions",
        ),
        migrations.RenameField(
            model_name="leave",
            old_name="end_date",
            new_name="end_time",
        ),
    ]
