# Generated by Django 3.2 on 2021-05-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_auto_20210504_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.TimeField()),
                ('end_day', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateField(auto_created=True, default='2021-05-05'),
        ),
    ]