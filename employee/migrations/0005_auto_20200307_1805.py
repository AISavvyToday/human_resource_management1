# Generated by Django 2.1.7 on 2020-03-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20200307_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='foccupation',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='moccupation',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='occupation',
        ),
    ]
