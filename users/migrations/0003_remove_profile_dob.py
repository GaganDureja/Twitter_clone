# Generated by Django 3.1 on 2021-01-04 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210104_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dob',
        ),
    ]