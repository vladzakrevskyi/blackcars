# Generated by Django 3.0.8 on 2021-09-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0085_auto_20210913_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='limit_per_two_weeks',
            field=models.CharField(default='2 100 km', max_length=10, verbose_name='Limit 2 tygodnie'),
        ),
        migrations.AlterField(
            model_name='car',
            name='limit_per_week',
            field=models.CharField(default='1 400 km', max_length=10, verbose_name='Limit tygodniowo'),
        ),
    ]