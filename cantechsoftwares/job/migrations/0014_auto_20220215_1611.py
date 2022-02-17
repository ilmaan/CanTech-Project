# Generated by Django 3.2.9 on 2022-02-15 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_alter_usermodel_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitermodel',
            name='status',
            field=models.CharField(blank=True, default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 15, 16, 11, 12, 20469)),
        ),
    ]