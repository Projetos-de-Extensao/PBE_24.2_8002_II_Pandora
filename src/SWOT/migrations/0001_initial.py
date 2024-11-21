# Generated by Django 5.1.3 on 2024-11-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Swot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='Temporary User', max_length=255)),
                ('strength', models.CharField(max_length=100)),
                ('weakness', models.CharField(max_length=100)),
                ('opportunity', models.CharField(max_length=100)),
                ('threat', models.CharField(max_length=100)),
                ('swot_analysis', models.CharField(max_length=100)),
                ('last_analysis_date', models.DateTimeField(auto_now_add=True)),
                ('analysis_period', models.IntegerField()),
                ('completion_status', models.BooleanField()),
            ],
        ),
    ]