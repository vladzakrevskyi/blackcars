# Generated by Django 3.1.7 on 2021-04-13 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0040_car_my_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='show_on_home',
            field=models.BooleanField(default=False),
        ),
    ]
