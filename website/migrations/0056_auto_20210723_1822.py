# Generated by Django 3.1.7 on 2021-07-23 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0055_extraoptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extraoptions',
            old_name='carKey',
            new_name='samochod',
        ),
    ]