# Generated by Django 3.0.8 on 2021-08-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0070_auto_20210802_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='slug_car',
            field=models.SlugField(unique=True, verbose_name='Link strony'),
        ),
    ]
