# Generated by Django 3.2.9 on 2022-02-20 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cantech', '0002_quotationmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotationmodel',
            old_name='qnoofpages',
            new_name='totalpage',
        ),
    ]
