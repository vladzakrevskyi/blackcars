# Generated by Django 3.0.8 on 2021-08-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0069_auto_20210802_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_rent_deposit',
            field=models.BooleanField(default=False, verbose_name='Kaucja przy opłacie kartą?'),
        ),
    ]
