# Generated by Django 3.0.3 on 2020-06-09 19:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200609_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 19, 56, 22, 825201, tzinfo=utc)),
        ),
    ]
