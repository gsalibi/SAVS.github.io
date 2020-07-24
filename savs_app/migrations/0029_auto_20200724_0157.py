# Generated by Django 3.0.6 on 2020-07-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0028_auto_20200724_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymouscomplaint',
            name='anonymous_race',
            field=models.TextField(choices=[('Branco(a)', 'Branco(a)'), ('Preto(a)', 'Preto(a)'), ('Amarelo(a) ', 'Amarelo(a)'), ('Indígena', 'Indígena'), ('Prefiro não responder', 'Prefiro não responder')], default=None),
        ),
        migrations.AlterField(
            model_name='identifiedcomplaint',
            name='identified_race',
            field=models.TextField(choices=[('Branco(a)', 'Branco(a)'), ('Preto(a)', 'Preto(a)'), ('Amarelo(a) ', 'Amarelo(a)'), ('Indígena', 'Indígena'), ('Prefiro não responder', 'Prefiro não responder')], default=None),
        ),
    ]