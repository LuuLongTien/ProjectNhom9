# Generated by Django 4.0.2 on 2022-04-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getchamp', '0005_champion_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='Team',
        ),
        migrations.AddField(
            model_name='champion',
            name='Team',
            field=models.ManyToManyField(to='getchamp.TeamBuilder'),
        ),
    ]
