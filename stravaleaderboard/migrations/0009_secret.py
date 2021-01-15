# Generated by Django 3.1.5 on 2021-01-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stravaleaderboard', '0008_auto_20210114_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField(default=0)),
                ('client_secret', models.TextField(max_length=200)),
                ('access_token', models.TextField(max_length=200)),
                ('refresh_token', models.TextField(max_length=200)),
            ],
        ),
    ]