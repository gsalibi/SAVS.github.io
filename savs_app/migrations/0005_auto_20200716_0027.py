# Generated by Django 3.0.6 on 2020-07-16 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0004_auto_20200716_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='complaint_person',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='where_happened',
        ),
        migrations.DeleteModel(
            name='UniversityPlace',
        ),
        migrations.DeleteModel(
            name='Complaint',
        ),
        migrations.DeleteModel(
            name='ComplaintPerson',
        ),
        migrations.DeleteModel(
            name='WhereHappened',
        ),
    ]
