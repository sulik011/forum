# Generated by Django 3.1 on 2020-10-01 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20201001_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
    ]