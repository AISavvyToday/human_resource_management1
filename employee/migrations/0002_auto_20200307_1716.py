# Generated by Django 2.1.7 on 2020-03-07 14:16

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='ssnitnumber',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='tinnumber',
        ),
        migrations.AddField(
            model_name='employee',
            name='nhifnumber',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='NHIF Number'),
        ),
        migrations.AddField(
            model_name='employee',
            name='nssfnumber',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='NSSF Number'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='education',
            field=models.CharField(choices=[('High School', 'High School'), ('Primary', 'Primary School'), ('Tertiary', 'Tertiary/University/Polytechnic/MA/PhD'), ('O-LEVEL', 'OLevel'), ('Other', 'Other')], default='Tertiary', help_text='highest educational standard ie. your last level of schooling', max_length=20, null=True, verbose_name='Education'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='region',
            field=models.CharField(choices=[('Coast', 'Coast'), ('Central', 'Central'), ('Eastern', 'Eastern'), ('North Eastern', 'North Eastern'), ('Rift Valley', 'Rift Valley'), ('Nairobi', 'Nairobi'), ('Western', 'Western'), ('Nyanza', 'Nyanza')], default='Nairobi', help_text='what region of the country(Kenya) are you from ?', max_length=20, null=True, verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+2540000000', help_text='Enter number with Country Code Eg. +233240000000', max_length=128, region=None, verbose_name='Phone Number (Example +233240000000)'),
        ),
    ]