# Generated by Django 3.0.3 on 2020-06-09 20:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200609_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
