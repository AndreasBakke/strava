# Generated by Django 3.1.5 on 2021-01-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stravaleaderboard', '0014_auto_20210121_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='currentpoints',
            field=models.IntegerField(default=0),
        ),
    ]
