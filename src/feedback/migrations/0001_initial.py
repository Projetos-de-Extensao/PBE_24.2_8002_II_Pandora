from django.db import migrations, models
from django.conf import settings  

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),  
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('suggestion', 'Suggestion for Improvement'), ('technical_issue', 'Technical Issue'), ('general_feedback', 'General Feedback')], max_length=60)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Detailed Feedback')),
                ('reporter', models.ForeignKey(on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)), 
            ],
        ),
        migrations.CreateModel(
            name='FeedbackAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.ForeignKey(on_delete=models.CASCADE, to='yourapp.platformfeedback')),  
                ('analysis_date', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(verbose_name='Analysis Notes')),
                ('status', models.CharField(choices=[('pending', 'Pending Review'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')], max_length=30)),
            ],
        ),
    ]
