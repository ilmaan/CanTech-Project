# Generated by Django 3.2.9 on 2022-02-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
