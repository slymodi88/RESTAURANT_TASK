# Generated by Django 3.2 on 2021-05-03 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='emp_number',
            new_name='employee_number',
        ),
    ]
