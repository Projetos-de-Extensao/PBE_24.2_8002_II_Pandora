# Generated by Django 5.1.3 on 2024-11-21 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0010_remove_feedbackanalysis_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackanalysis',
            name='analyst',
        ),
        migrations.AddField(
            model_name='feedbackanalysis',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Analyst'),
        ),
    ]
