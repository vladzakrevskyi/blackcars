# Generated by Django 3.0.8 on 2021-07-30 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0067_auto_20210730_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='is_deposit_2',
            new_name='is_rent_deposit',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='deposit_2',
            new_name='rent_deposit',
        ),
    ]
