# Generated by Django 3.0.3 on 2020-06-09 19:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200609_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 6, 9, 19, 51, 29, 158190, tzinfo=utc)),
        ),
    ]
