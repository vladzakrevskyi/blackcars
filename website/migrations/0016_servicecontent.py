# Generated by Django 3.1.7 on 2021-03-13 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_remove_sliderimage_image_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Wybierz zdjęcie', null=True, upload_to='service_images', verbose_name='Zdjecie bloku')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Tytuł bloku')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Zawartość bloku')),
                ('service_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.service')),
            ],
            options={
                'verbose_name': 'Tekstowy blok',
                'verbose_name_plural': 'Tekstowe bloki',
            },
        ),
    ]
