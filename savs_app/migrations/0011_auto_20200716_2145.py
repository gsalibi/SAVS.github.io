# Generated by Django 3.0.6 on 2020-07-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0010_auto_20200716_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymouscomplaint',
            name='complainer_connection_unicamp',
            field=models.TextField(choices=[('graduate', 'Aluna(o) de graduação'), ('postgraduate', 'Aluna(o) de pós-graduação'), ('outsourced', 'Terceirizada(o)'), ('professor', 'Docente'), ('another', 'Outro'), ('not_unicamp', 'Não tenho vínculo com a universidade')], default=None),
        ),
        migrations.AlterField(
            model_name='anonymouscomplaint',
            name='complainer_gender',
            field=models.TextField(choices=[('woman', 'Mulher (trans ou cis)'), ('man', 'Homem (trans ou cis)'), ('non_binary', 'Gênero Não-binário'), ('another', 'Outro'), ('no_answer', 'Prefiro não responder')], default=None),
        ),
        migrations.AlterField(
            model_name='anonymouscomplaint',
            name='complainer_support_requested',
            field=models.TextField(choices=[('yes', 'Sim'), ('no', 'Não'), ('dont_know', 'Não sei dizer')], default=None),
        ),
        migrations.AlterField(
            model_name='anonymouscomplaint',
            name='complainer_why_anonymous',
            field=models.TextField(choices=[('victim_dont_want', 'Porque a pessoa que vivenciou o episódio não quer fazer uma queixa'), ('fear', 'Porque tenho medo de retaliações que possam prejudicar a minha carreira e/ou a minha vida acadêmica'), ('dont_want_orientations', 'Porque não quero receber apoio e orientações do SAVS'), ('just_inform', 'Porque meu objetivo é que a universidade apenas tenha conhecimento deste episódio'), ('another', 'Outro')], default=None),
        ),
        migrations.AlterField(
            model_name='anonymouscomplaint',
            name='episode_date',
            field=models.TextField(choices=[('last_week', 'Na semana passada'), ('last_mounth', 'No mês passado'), ('las_yar', 'No ano passado'), ('exact', 'Eu sei a data exata'), ('dont_know', 'Não sei')], default=None),
        ),
        migrations.AlterField(
            model_name='anonymouscomplaint',
            name='episode_date_period',
            field=models.TextField(choices=[('morning', 'Manhã'), ('afternoon', 'Tarde'), ('night', 'Noite'), ('dawn', 'Madrugada'), ('exact', 'Eu sei o horário exato'), ('dont_know', 'Não sei')], default=None),
        ),
        migrations.AlterField(
            model_name='identifiedcomplaint',
            name='complainer_connection_unicamp',
            field=models.TextField(choices=[('graduate', 'Aluna(o) de graduação'), ('postgraduate', 'Aluna(o) de pós-graduação'), ('outsourced', 'Terceirizada(o)'), ('professor', 'Docente'), ('another', 'Outro'), ('not_unicamp', 'Não tenho vínculo com a universidade')], default=None),
        ),
        migrations.AlterField(
            model_name='identifiedcomplaint',
            name='complainer_gender',
            field=models.TextField(choices=[('woman', 'Mulher (trans ou cis)'), ('man', 'Homem (trans ou cis)'), ('non_binary', 'Gênero Não-binário'), ('another', 'Outro'), ('no_answer', 'Prefiro não responder')], default=None),
        ),
        migrations.AlterField(
            model_name='identifiedcomplaint',
            name='episode_date',
            field=models.TextField(choices=[('last_week', 'Na semana passada'), ('last_mounth', 'No mês passado'), ('las_yar', 'No ano passado'), ('exact', 'Eu sei a data exata'), ('dont_know', 'Não sei')], default=None),
        ),
        migrations.AlterField(
            model_name='identifiedcomplaint',
            name='episode_date_period',
            field=models.TextField(choices=[('morning', 'Manhã'), ('afternoon', 'Tarde'), ('night', 'Noite'), ('dawn', 'Madrugada'), ('exact', 'Eu sei o horário exato'), ('dont_know', 'Não sei')], default=None),
        ),
    ]
