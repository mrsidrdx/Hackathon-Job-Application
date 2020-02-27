# Generated by Django 3.0.1 on 2020-02-27 19:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0007_auto_20200227_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='review',
            name='job_description',
            field=models.FileField(upload_to='documents'),
        ),
    ]