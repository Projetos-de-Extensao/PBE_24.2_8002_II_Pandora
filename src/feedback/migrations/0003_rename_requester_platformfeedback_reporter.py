# Generated by Django 5.1.3 on 2024-11-20 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_remove_platformfeedback_submission_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platformfeedback',
            old_name='requester',
            new_name='requester',
        ),
    ]