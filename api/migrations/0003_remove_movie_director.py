# Generated by Django 3.0.5 on 2020-04-13 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
    ]
