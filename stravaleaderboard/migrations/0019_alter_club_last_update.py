# Generated by Django 4.0.1 on 2022-01-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stravaleaderboard', '0018_auto_20210121_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='last_update',
            field=models.IntegerField(default=1615158000),
        ),
    ]
