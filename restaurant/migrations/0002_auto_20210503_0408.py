# Generated by Django 3.1.7 on 2021-05-03 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='chk1',
        ),
        migrations.RemoveField(
            model_name='food',
            name='chk2',
        ),
        migrations.RemoveField(
            model_name='food',
            name='chk3',
        ),
        migrations.RemoveField(
            model_name='food',
            name='cuisine',
        ),
        migrations.RemoveField(
            model_name='food',
            name='price',
        ),
        migrations.RemoveField(
            model_name='food',
            name='radio',
        ),
    ]
