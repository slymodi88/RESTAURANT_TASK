# Generated by Django 3.2 on 2021-05-03 20:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('emp_number', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(6, 'Password must be at least 6 characters long')])),
            ],
        ),
    ]
