# Generated by Django 2.1 on 2018-08-13 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_active',
        ),
    ]
