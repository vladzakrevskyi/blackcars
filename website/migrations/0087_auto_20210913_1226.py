# Generated by Django 3.0.8 on 2021-09-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0086_auto_20210913_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='limit_per_two_weeks',
            field=models.CharField(default='2 100 km', max_length=10, verbose_name='Limit dwa tygodnie'),
        ),
    ]
