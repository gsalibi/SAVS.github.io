# Generated by Django 3.0.6 on 2020-07-18 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0020_auto_20200718_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complainer_connection_unicamp',
            new_name='anonymous_connection_unicamp',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complainer_connection_unicamp_complement',
            new_name='anonymous_connection_unicamp_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='episode_date',
            new_name='anonymous_episode_date',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='episode_date_complement',
            new_name='anonymous_episode_date_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='episode_date_period',
            new_name='anonymous_episode_date_period',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='episode_date_period_complement',
            new_name='anonymous_episode_date_period_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='episode_location',
            new_name='anonymous_episode_location',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='episode_location_complement',
            new_name='anonymous_episode_location_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='episode_report',
            new_name='anonymous_episode_report',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complainer_gender',
            new_name='anonymous_gender',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complainer_gender_complement',
            new_name='anonymous_gender_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complainer_position',
            new_name='anonymous_position',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complainer_position_complement',
            new_name='anonymous_position_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complainer_support_requested',
            new_name='anonymous_support_requested',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complainer_support_requested_complement',
            new_name='anonymous_support_requested_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complainer_why_anonymous',
            new_name='anonymous_why_anonymous',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complainer_why_anonymous_complement',
            new_name='anonymous_why_anonymous_complement',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_address',
            new_name='identified_address',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_address_number',
            new_name='identified_address_number',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_city',
            new_name='identified_city',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_identified_connection_unicamp',
            new_name='identified_connection_unicamp',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_identified_connection_unicamp_complement',
            new_name='identified_connection_unicamp_complement',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_course',
            new_name='identified_course',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_cpf',
            new_name='identified_cpf',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_email',
            new_name='identified_email',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='episode_date',
            new_name='identified_episode_date',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='episode_date_complement',
            new_name='identified_episode_date_complement',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='episode_date_period',
            new_name='identified_episode_date_period',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='episode_date_period_complement',
            new_name='identified_episode_date_period_complement',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='episode_location',
            new_name='identified_episode_location',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='episode_location_complement',
            new_name='identified_episode_location_complement',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='episode_report',
            new_name='identified_episode_report',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_gender',
            new_name='identified_gender',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_gender_complement',
            new_name='identified_gender_complement',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_institute',
            new_name='identified_institute',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_is_social_name',
            new_name='identified_is_social_name',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_name',
            new_name='identified_name',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_neighborhood',
            new_name='identified_neighborhood',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_position',
            new_name='identified_position',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_position_complement',
            new_name='identified_position_complement',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_ra',
            new_name='identified_ra',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_state',
            new_name='identified_state',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_telephone',
            new_name='identified_telephone',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complainer_zipcode',
            new_name='identified_zipcode',
        ),
    ]
