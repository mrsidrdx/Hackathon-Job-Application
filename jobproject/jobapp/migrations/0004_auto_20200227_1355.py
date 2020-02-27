# Generated by Django 3.0.1 on 2020-02-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_auto_20200227_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='job_role',
            field=models.CharField(choices=[('SE', 'Software Engineer'), ('AE', 'Automobile Engineer'), ('DS', 'Data Scientist'), ('BD', 'Backend Developer'), ('FD', 'Frontend Developer'), ('FSD', 'Full Stack Developer'), ('SE', 'System Engineer'), ('DE', 'DevOps Enginner')], max_length=40),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_type',
            field=models.CharField(choices=[('FT', 'Full Time'), ('I', 'Intership'), ('WFH', 'Work From Home')], max_length=20),
        ),
    ]
