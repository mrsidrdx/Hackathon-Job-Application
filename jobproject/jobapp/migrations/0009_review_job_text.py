# Generated by Django 3.0.1 on 2020-02-27 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0008_auto_20200228_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='job_text',
            field=models.TextField(default=None),
        ),
    ]
