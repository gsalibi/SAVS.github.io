# Generated by Django 3.0.6 on 2020-07-24 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0026_auto_20200724_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymouscomplaint',
            name='anonymous_episode_date',
            field=models.TextField(choices=[('Eu sei a data exata', 'Eu sei a data exata'), ('Eu não sei a data exata, mas sei aproximadamente', 'Eu não sei a data exata, mas sei aproximadamente'), ('Não há uma data específica, pois são episódios recorrentes, que continuam acontecendo', 'Não há uma data específica, pois são episódios recorrentes, que continuam acontecendo'), ('Não há uma data específica, pois eram episódios recorrentes, mas que já deixaram de acontecer', 'Não há uma data específica, pois eram episódios recorrentes, mas que já deixaram de acontecer'), ('Outro', 'Outro')], default=None),
        ),
        migrations.AlterField(
            model_name='anonymouscomplaint',
            name='anonymous_episode_date_period',
            field=models.TextField(choices=[('Eu sei o horário exato', 'Eu sei o horário exato'), ('Eu não sei o horário, mas sei aproximadamente', 'Eu não sei o horário, mas sei aproximadamente'), ('Não há um horário específico, pois tratam-se de episódios recorrentes. ', 'Não há um horário específico, pois tratam-se de episódios recorrentes. '), ('Não sei o horário', 'Não sei o horário')], default=None),
        ),
        migrations.AlterField(
            model_name='anonymouscomplaint',
            name='anonymous_episode_location',
            field=models.TextField(choices=[('Na universidade', 'Na universidade'), ('Na minha casa', 'Na minha casa'), ('Em uma festa', 'Em uma festa'), ('Outro', 'Outro'), ('Foram em vários lugares', 'Foram em vários lugares'), ('Não foi em um local físico, foi online', 'Não foi em um local físico, foi online'), ('Não sei o local', 'Não sei o local')], default=None),
        ),
        migrations.AlterField(
            model_name='identifiedcomplaint',
            name='identified_episode_date',
            field=models.TextField(choices=[('Eu sei a data exata', 'Eu sei a data exata'), ('Eu não sei a data exata, mas sei aproximadamente', 'Eu não sei a data exata, mas sei aproximadamente'), ('Não há uma data específica, pois são episódios recorrentes, que continuam acontecendo', 'Não há uma data específica, pois são episódios recorrentes, que continuam acontecendo'), ('Não há uma data específica, pois eram episódios recorrentes, mas que já deixaram de acontecer', 'Não há uma data específica, pois eram episódios recorrentes, mas que já deixaram de acontecer'), ('Outro', 'Outro')], default=None),
        ),
        migrations.AlterField(
            model_name='identifiedcomplaint',
            name='identified_episode_date_period',
            field=models.TextField(choices=[('Eu sei o horário exato', 'Eu sei o horário exato'), ('Eu não sei o horário, mas sei aproximadamente', 'Eu não sei o horário, mas sei aproximadamente'), ('Não há um horário específico, pois tratam-se de episódios recorrentes. ', 'Não há um horário específico, pois tratam-se de episódios recorrentes. '), ('Não sei o horário', 'Não sei o horário')], default=None),
        ),
        migrations.AlterField(
            model_name='identifiedcomplaint',
            name='identified_episode_location',
            field=models.TextField(choices=[('Na universidade', 'Na universidade'), ('Na minha casa', 'Na minha casa'), ('Em uma festa', 'Em uma festa'), ('Outro', 'Outro'), ('Foram em vários lugares', 'Foram em vários lugares'), ('Não foi em um local físico, foi online', 'Não foi em um local físico, foi online'), ('Não sei o local', 'Não sei o local')], default=None),
        ),
    ]
