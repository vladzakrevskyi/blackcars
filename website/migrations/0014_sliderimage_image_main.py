# Generated by Django 3.1.7 on 2021-03-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_sliderimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='image_main',
            field=models.ImageField(blank=True, help_text='Główne djecie samochodu', null=True, upload_to='slider_images', verbose_name='Główne zdjecie samochodu'),
        ),
    ]