# Generated by Django 3.0.6 on 2020-07-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0018_envolvedperson_person_information_complement'),
    ]

    operations = [
        migrations.AddField(
            model_name='identifiedcomplaint',
            name='complainer_address_number',
            field=models.TextField(default=None),
        ),
    ]