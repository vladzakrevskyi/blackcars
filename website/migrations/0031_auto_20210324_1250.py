# Generated by Django 3.1.7 on 2021-03-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_auto_20210324_0734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='image',
        ),
        migrations.AddField(
            model_name='option',
            name='icon',
            field=models.CharField(blank=True, max_length=300, verbose_name='Ikona'),
        ),
    ]
