# Generated by Django 3.0.6 on 2020-07-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0017_auto_20200717_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='envolvedperson',
            name='person_information_complement',
            field=models.TextField(blank=True, null=True),
        ),
    ]
