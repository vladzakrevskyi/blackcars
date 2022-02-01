# Generated by Django 3.0.8 on 2021-07-24 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0063_auto_20210723_2014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extraoptions',
            options={'ordering': ['car'], 'verbose_name': 'Opcja dodatkowa', 'verbose_name_plural': 'Opcje dodatkowe'},
        ),
        migrations.RemoveField(
            model_name='extraoptions',
            name='samochod',
        ),
        migrations.AddField(
            model_name='extraoptions',
            name='car',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='car_key', to='website.Car'),
            preserve_default=False,
        ),
    ]
