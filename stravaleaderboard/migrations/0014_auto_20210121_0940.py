# Generated by Django 3.1.5 on 2021-01-21 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stravaleaderboard', '0013_auto_20210115_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='distances',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
