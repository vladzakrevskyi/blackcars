# Generated by Django 3.0.8 on 2021-09-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0083_car_promotion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-promotion', 'my_order'], 'verbose_name': 'Samochód', 'verbose_name_plural': 'Samochody'},
        ),
        migrations.RemoveField(
            model_name='option',
            name='icon',
        ),
        migrations.AlterField(
            model_name='car',
            name='promotion',
            field=models.IntegerField(blank=True, help_text='W procentach (%)', null=True, verbose_name='Promocja (w %)'),
        ),
    ]
