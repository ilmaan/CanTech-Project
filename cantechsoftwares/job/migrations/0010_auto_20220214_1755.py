# Generated by Django 3.2.9 on 2022-02-14 12:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0009_alter_usermodel_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 17, 55, 59, 191222)),
        ),
        migrations.CreateModel(
            name='RecruiterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(blank=True, max_length=100, null=True)),
                ('uphone', models.CharField(blank=True, max_length=13, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
