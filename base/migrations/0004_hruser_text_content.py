# Generated by Django 5.0.1 on 2024-02-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_user_id_resume_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hruser',
            name='text_content',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
