# Generated by Django 3.2.4 on 2021-06-27 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesman', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesman',
            name='sells',
        ),
        migrations.RemoveField(
            model_name='salesman',
            name='sells_numbers',
        ),
    ]
