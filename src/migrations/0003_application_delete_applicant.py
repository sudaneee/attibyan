# Generated by Django 5.1.5 on 2025-02-01 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_applicant_delete_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('category', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=15)),
                ('optional_courses', models.JSONField()),
                ('preferred_time', models.CharField(blank=True, max_length=50, null=True)),
                ('motivation', models.TextField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='applications/profile_pics/')),
                ('certificates', models.FileField(blank=True, null=True, upload_to='applications/certificates/')),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Applicant',
        ),
    ]
