# Generated by Django 2.1 on 2018-10-01 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_feesummary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentfee',
            name='month',
        ),
        migrations.RemoveField(
            model_name='studentfee',
            name='year',
        ),
        migrations.AddField(
            model_name='studentfee',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 10, 1, 18, 42, 4, 610995)),
        ),
    ]