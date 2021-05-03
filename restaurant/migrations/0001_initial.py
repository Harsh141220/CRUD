# Generated by Django 3.1.7 on 2021-05-03 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('name', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('des', models.TextField()),
                ('cuisine', models.CharField(max_length=150)),
                ('chk1', models.BooleanField(default=False)),
                ('chk2', models.BooleanField(default=False)),
                ('chk3', models.BooleanField(default=False)),
                ('dat', models.DateField(auto_now=True)),
                ('radio', models.CharField(max_length=150)),
                ('img', models.FileField(upload_to='pic')),
            ],
        ),
    ]
