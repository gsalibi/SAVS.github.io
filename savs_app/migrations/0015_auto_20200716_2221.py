# Generated by Django 3.0.6 on 2020-07-16 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0014_auto_20200716_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='identifiedcomplaint',
            name='episode_date_complement',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='identifiedcomplaint',
            name='episode_date_period_complement',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='identifiedcomplaint',
            name='episode_location_complement',
            field=models.TextField(null=True),
        ),
    ]
