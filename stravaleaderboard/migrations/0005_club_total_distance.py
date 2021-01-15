# Generated by Django 3.1.5 on 2021-01-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stravaleaderboard', '0004_delete_total_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='total_distance',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=200),
        ),
    ]
