# Generated by Django 2.1.4 on 2018-12-24 22:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 24, 22, 39, 7, 869050, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 24, 22, 39, 7, 868053, tzinfo=utc)),
        ),
    ]
