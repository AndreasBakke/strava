# Generated by Django 4.0.1 on 2022-01-28 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stravaleaderboard', '0021_club_percentage_alter_club_last_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='percentage',
        ),
    ]
