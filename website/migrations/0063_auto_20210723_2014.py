# Generated by Django 3.1.7 on 2021-07-23 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0062_auto_20210723_2013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extraoptions',
            options={'ordering': ['samochod'], 'verbose_name': 'Opcja dodatkowa', 'verbose_name_plural': 'Opcje dodatkowe'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='extraoptions',
            order_with_respect_to=None,
        ),
    ]
