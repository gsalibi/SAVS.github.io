# Generated by Django 3.0.6 on 2020-07-17 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0016_auto_20200717_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='envolvedperson',
            old_name='is_author',
            new_name='is_accused',
        ),
    ]
