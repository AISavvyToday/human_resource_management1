# Generated by Django 2.1.7 on 2020-03-05 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField(help_text='leave start date is on ..', null=True, verbose_name='Start Date')),
                ('enddate', models.DateField(help_text='coming back on ...', null=True, verbose_name='End Date')),
                ('leavetype', models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'Casual Leave'), ('emergency', 'Emergency Leave'), ('study', 'Study Leave')], default='sick', max_length=25, null=True)),
                ('reason', models.CharField(blank=True, help_text='add additional information for leave', max_length=255, null=True, verbose_name='Reason for Leave')),
                ('defaultdays', models.PositiveIntegerField(blank=True, default=30, null=True, verbose_name='Leave days per year counter')),
                ('status', models.CharField(default='pending', max_length=12)),
                ('is_approved', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Leave',
                'verbose_name_plural': 'Leaves',
                'ordering': ['-created'],
            },
        ),
    ]
