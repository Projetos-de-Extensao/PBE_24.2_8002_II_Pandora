# Generated by Django 5.1.3 on 2024-11-20 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiencia', models.CharField(default='No experience', max_length=255)),
                ('carreira_atual', models.CharField(default='No current career', max_length=255)),
            ],
        ),
    ]