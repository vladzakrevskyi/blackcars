# Generated by Django 3.1.7 on 2021-07-23 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0061_extraoptions'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='extraoptions',
            order_with_respect_to='samochod',
        ),
    ]
