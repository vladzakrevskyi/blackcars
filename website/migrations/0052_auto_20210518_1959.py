# Generated by Django 3.0.8 on 2021-05-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0051_auto_20210504_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option_reservation',
            name='choise',
            field=models.CharField(choices=[('W cenie', 'W cenie'), ('Dodatkowa cena', 'Dodatkowa cena')], default='Dodatkowa cena', max_length=100, verbose_name='Rodzaj ceny'),
        ),
    ]
