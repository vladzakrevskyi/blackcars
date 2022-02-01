# Generated by Django 3.1.7 on 2021-03-11 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210311_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200, verbose_name='Model samochodu')),
                ('price', models.CharField(max_length=10, verbose_name='Cena za wynajem')),
                ('car_photo', models.ImageField(blank=True, help_text='Zdjecie samochodu', null=True, upload_to='car_image_small', verbose_name='Zdjęcie samochodu')),
                ('slug', models.SlugField(default='slug', unique=True)),
            ],
            options={
                'verbose_name': 'Samochód',
                'verbose_name_plural': 'Samochody',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(blank=True, max_length=200, null=True, verbose_name='Wyposażenie')),
                ('options', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.car')),
            ],
            options={
                'verbose_name': 'Wyposażenie samochodu',
                'verbose_name_plural': 'Wyposażenia samochodu',
            },
        ),
    ]
