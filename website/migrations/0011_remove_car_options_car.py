# Generated by Django 3.1.7 on 2021-03-12 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_car_options_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='options_car',
        ),
    ]